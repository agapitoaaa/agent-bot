import os, sys, json, tempfile, shutil, unittest, io, contextlib
HERE = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "scripts"))

class T(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        os.makedirs(os.path.join(self.tmp, "memory"))
        shutil.copy(os.path.join(HERE, "..", "policy.json"), os.path.join(self.tmp, "memory", "policy.json"))
        os.environ["TRADING_DIR"] = self.tmp
        if "trade_memory" in sys.modules:
            del sys.modules["trade_memory"]
        import trade_memory
        self.m = trade_memory

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def run_cmd(self, *args):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            self.m.main(list(args))
        return buf.getvalue().strip()

    def decision(self, strat="trend", conf="0.7"):
        return self.run_cmd("add-decision", "--strategy", strat, "--instrument", "SPY", "--action", "buy", "--size-pct", "5",
                            "--rationale", "above 200d", "--invalidation", "close below 200d", "--counter", "whipsaw risk",
                            "--confidence", conf)

    def test_decision_requires_counter_and_invalidation(self):
        with self.assertRaises(SystemExit):
            self.run_cmd("add-decision", "--strategy", "t", "--instrument", "SPY", "--action", "buy", "--rationale", "x", "--counter", "y")
        did = self.decision()
        self.assertTrue(did.startswith("d-"))

    def test_outcome_once_only(self):
        d = self.decision()
        self.run_cmd("add-outcome", "--decision", d, "--pnl-net-pct", "1.5", "--benchmark-pct", "1.0")
        with self.assertRaises(SystemExit):
            self.run_cmd("add-outcome", "--decision", d, "--pnl-net-pct", "2")

    def test_lesson_promotion_is_gated(self):
        ids = [self.decision() for _ in range(12)]
        lid = self.run_cmd("add-lesson", "--text", "Avoid trading when vol is in top decile").split()[0]
        with self.assertRaises(SystemExit):
            self.run_cmd("promote", "--id", lid, "--to", "candidate", "--support", *ids[:2])
        self.run_cmd("promote", "--id", lid, "--to", "candidate", "--support", *ids[:3])
        with self.assertRaises(SystemExit):
            self.run_cmd("promote", "--id", lid, "--to", "rule", "--support", *ids[:10])  # no QA review
        self.run_cmd("promote", "--id", lid, "--to", "rule", "--support", *ids[:10], "--qa-reviewed")
        self.assertEqual(self.m.lessons_state()[lid]["status"], "rule")

    def test_promotion_needs_real_decisions(self):
        lid = self.run_cmd("add-lesson", "--text", "x").split()[0]
        with self.assertRaises(SystemExit):
            self.run_cmd("promote", "--id", lid, "--to", "candidate", "--support", "d-fake-1", "d-fake-2", "d-fake-3")

    def test_scorecard_flags_small_samples_and_calibration(self):
        for pnl in (2.0, -1.0, 0.5):
            d = self.decision(conf="0.8")
            self.run_cmd("add-outcome", "--decision", d, "--pnl-net-pct", str(pnl), "--benchmark-pct", "0.5")
        sc = self.m.scorecard()
        self.assertEqual(sc[0]["n_closed"], 3)
        self.assertFalse(sc[0]["sample_ok"])
        cal = self.m.calibration()
        self.assertEqual(cal["n"], 3)
        self.assertAlmostEqual(cal["brier"], ((0.2) ** 2 + (0.8) ** 2 + (0.2) ** 2) / 3)
        text = self.m.render(write=True)
        self.assertIn("WARNING", text)
        self.assertTrue(os.path.exists(os.path.join(self.tmp, "memory", "rules.md")))

if __name__ == "__main__":
    unittest.main()
