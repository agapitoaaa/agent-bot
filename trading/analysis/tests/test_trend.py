import os, sys, unittest, tempfile, datetime
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import trend

def make_rows(n, f, start=datetime.date(2022, 1, 3)):
    rows, d = [], start
    for i in range(n):
        while d.weekday() >= 5:
            d += datetime.timedelta(days=1)
        c = f(i)
        rows.append({"date": d.isoformat(), "high": c * 1.01, "low": c * 0.99, "close": c})
        d += datetime.timedelta(days=1)
    return rows

class T(unittest.TestCase):
    def test_sma_and_returns(self):
        self.assertEqual(trend.sma([1, 2, 3, 4], 2), 3.5)
        self.assertIsNone(trend.sma([1], 2))
        self.assertAlmostEqual(trend.pct_returns([100, 110])[0], 0.1)

    def test_max_drawdown(self):
        self.assertAlmostEqual(trend.max_drawdown([100, 120, 90, 130]), 90 / 120 - 1)

    def test_uptrend_and_downtrend(self):
        up = trend.analyze(make_rows(300, lambda i: 100 + i * 0.5))
        dn = trend.analyze(make_rows(300, lambda i: 300 - i * 0.5))
        self.assertEqual(up["trend_state"], "uptrend")
        self.assertEqual(dn["trend_state"], "downtrend")
        self.assertGreater(up["momentum_12_1"], 0)
        self.assertLess(dn["momentum_12_1"], 0)

    def test_as_of_has_no_lookahead(self):
        rows = make_rows(320, lambda i: 100 + (i % 40) * 0.8 + i * 0.1)
        cut = rows[250]["date"]
        a = trend.analyze(rows, as_of=cut)
        b = trend.analyze(rows[:251])
        self.assertEqual(a, b)
        self.assertEqual(a["data_through"], cut)

    def test_insufficient_data(self):
        self.assertEqual(trend.analyze(make_rows(10, lambda i: 100))["status"], "insufficient_data")

    def test_whipsaw_crosses(self):
        choppy = trend.analyze(make_rows(400, lambda i: 100 + (5 if i % 20 < 10 else -5)))
        smooth = trend.analyze(make_rows(400, lambda i: 100 + i * 0.3))
        self.assertGreater(choppy["sma200_crosses_last_year"], smooth["sma200_crosses_last_year"])

    def test_csv_roundtrip(self):
        with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False) as f:
            f.write("Date,Open,High,Low,Close\n")
            for r in make_rows(60, lambda i: 100 + i):
                f.write(f"{r['date']},{r['close']},{r['high']},{r['low']},{r['close']}\n")
        rows = trend.load_csv(f.name)
        os.unlink(f.name)
        self.assertEqual(len(rows), 60)
        self.assertEqual(trend.analyze(rows)["status"], "ok")

if __name__ == "__main__":
    unittest.main()
