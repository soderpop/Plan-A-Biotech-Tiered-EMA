# Plan A Biotech MVP

This repository contains a demonstration implementation of the **Tiered-EMA™ positional index**. The algorithm maintains a constant memory footprint while providing increasingly precise position estimates across multiple tiers.

Key properties of the index are described in `DESIGN.md`, including:

- Fixed memory usage of `8(K+1)` bytes regardless of stream length
- `O(K)` update complexity and `O(1)` query per tier
- Bias correction via closed-form solution

The `plan_a_mvp.py` script simulates a stream of events and prints the tier
values just like in the pitch deck.  For each tier it displays the raw EMA, the
bias‑corrected estimate and the closed‑form solution so you can confirm they
match.  Run it with:

```bash
python3 plan_a_mvp.py --events 50000 --tiers 20
```

This processes 50,000 events and reports the constant memory usage along with a
table of the first few tiers.
