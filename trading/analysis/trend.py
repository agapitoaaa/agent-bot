#!/usr/bin/env python3
"""Descriptive trend analysis for Ledger. Stdlib only.

Reads daily OHLC CSV (columns: date,open,high,low,close[,volume]) and reports the trend state, momentum,
volatility, drawdown and whipsaw measures **using only data on or before --as-of** (no look-ahead).
This describes the market. It is NOT a trade signal: signals come only from pre-registered strategies.

usage: trend.py FILE.csv [FILE2.csv ...] [--as-of YYYY-MM-DD] [--json]
"""
import csv, json, math, sys, statistics, argparse, datetime

def load_csv(path):
    rows = []
    with open(path, newline="") as f:
        for r in csv.DictReader(f):
            r = {k.strip().lower(): v for k, v in r.items()}
            try:
                rows.append({"date": r["date"][:10], "high": float(r.get("high") or r["close"]),
                             "low": float(r.get("low") or r["close"]), "close": float(r["close"])})
            except (KeyError, ValueError):
                continue
    rows.sort(key=lambda x: x["date"])
    return rows

def sma(v, n):
    return sum(v[-n:]) / n if len(v) >= n else None

def pct_returns(v):
    return [v[i] / v[i - 1] - 1 for i in range(1, len(v)) if v[i - 1]]

def ann_vol(rets, n):
    if len(rets) < n:
        return None
    return statistics.pstdev(rets[-n:]) * math.sqrt(252)

def max_drawdown(v):
    peak, mdd = v[0], 0.0
    for x in v:
        peak = max(peak, x)
        mdd = min(mdd, x / peak - 1)
    return mdd

def momentum(v, lookback, skip=0):
    """Return from t-lookback to t-skip (e.g. 12-1 momentum: lookback=252, skip=21)."""
    if len(v) <= lookback:
        return None
    end = v[-1 - skip]
    return end / v[-1 - lookback] - 1

def crosses(v, n):
    """Number of times close crossed its n-day SMA in the last 252 bars (whipsaw measure)."""
    if len(v) < n + 2:
        return None
    window = v[-252:] if len(v) >= 252 + n else v[n:]
    start = len(v) - len(window)
    count, prev = 0, None
    for i in range(start, len(v)):
        m = sum(v[i - n + 1:i + 1]) / n
        above = v[i] > m
        if prev is not None and above != prev:
            count += 1
        prev = above
    return count

def percentile_rank(series, x):
    s = [a for a in series if a is not None]
    return None if not s else sum(1 for a in s if a <= x) / len(s)

def analyze(rows, as_of=None):
    if as_of:
        rows = [r for r in rows if r["date"] <= as_of]
    out = {"data_through": rows[-1]["date"] if rows else None, "bars": len(rows),
           "note": "Descriptive only. Not a trade signal."}
    if len(rows) < 30:
        out["status"] = "insufficient_data"
        return out
    c = [r["close"] for r in rows]
    hi = [r["high"] for r in rows]
    lo = [r["low"] for r in rows]
    rets = pct_returns(c)
    last = c[-1]
    m50, m200 = sma(c, 50), sma(c, 200)
    monthly = []
    for r in rows:  # last close of each month, for a 10-month MA
        ym = r["date"][:7]
        if monthly and monthly[-1][0] == ym:
            monthly[-1] = (ym, r["close"])
        else:
            monthly.append((ym, r["close"]))
    mclose = [x[1] for x in monthly]
    m10 = sma(mclose, 10)
    if m200 is not None and m50 is not None:
        state = "uptrend" if last > m200 and m50 > m200 else "downtrend" if last < m200 and m50 < m200 else "mixed"
    else:
        state = "unknown_short_history"
    slope = None
    if len(c) >= 220:
        slope = sma(c[:-20], 200) and m200 / sma(c[:-20], 200) - 1
    vol20 = ann_vol(rets, 20)
    vol_hist = [ann_vol(rets[:i], 20) for i in range(20, len(rets) + 1, 5)]
    window52 = c[-252:]
    gaps = sum(1 for i in range(1, len(rows)) if (datetime.date.fromisoformat(rows[i]["date"]) -
                                                  datetime.date.fromisoformat(rows[i - 1]["date"])).days > 5)
    out.update({
        "status": "ok", "last_close": last, "trend_state": state,
        "sma50": m50, "sma200": m200, "dist_to_sma200": (last / m200 - 1) if m200 else None,
        "monthly_sma10": m10, "above_monthly_sma10": (last > m10) if m10 else None,
        "sma200_slope_20d": slope,
        "momentum_12_1": momentum(c, 252, 21), "momentum_6m": momentum(c, 126), "momentum_3m": momentum(c, 63),
        "vol_20d_ann": vol20, "vol_60d_ann": ann_vol(rets, 60),
        "vol_20d_percentile": percentile_rank(vol_hist, vol20) if vol20 is not None else None,
        "drawdown_from_52w_high": last / max(window52) - 1,
        "max_drawdown_full_history": max_drawdown(c),
        "donchian55_breakout_up": last >= max(hi[-56:-1]) if len(hi) > 56 else None,
        "donchian55_breakdown": last <= min(lo[-56:-1]) if len(lo) > 56 else None,
        "sma200_crosses_last_year": crosses(c, 200),
        "data_quality": {"gaps_over_5_days": gaps, "enough_for_sma200": len(c) >= 200},
    })
    return out

def fmt(x, pct=False):
    if x is None:
        return "n/a"
    if isinstance(x, bool):
        return "yes" if x else "no"
    return f"{x*100:.1f}%" if pct else f"{x:.2f}"

def table(results):
    head = f"{'file':<22}{'through':<12}{'state':<22}{'vs200':>8}{'mom12-1':>9}{'vol20':>8}{'dd52w':>8}{'x200':>6}"
    lines = [head, "-" * len(head)]
    for name, a in results:
        if a.get("status") != "ok":
            lines.append(f"{name:<22}{a.get('data_through') or '-':<12}{a.get('status')}")
            continue
        lines.append(f"{name[:21]:<22}{a['data_through']:<12}{a['trend_state']:<22}"
                     f"{fmt(a['dist_to_sma200'],True):>8}{fmt(a['momentum_12_1'],True):>9}"
                     f"{fmt(a['vol_20d_ann'],True):>8}{fmt(a['drawdown_from_52w_high'],True):>8}"
                     f"{str(a['sma200_crosses_last_year']):>6}")
    lines.append("Descriptive only. Not a trade signal. Crosses of the 200-day SMA in the last year = whipsaw measure.")
    return "\n".join(lines)

def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("files", nargs="+")
    p.add_argument("--as-of")
    p.add_argument("--json", action="store_true")
    a = p.parse_args(argv)
    results = [(f.split("/")[-1], analyze(load_csv(f), a.as_of)) for f in a.files]
    print(json.dumps({n: r for n, r in results}, indent=2) if a.json else table(results))

if __name__ == "__main__":
    main()
