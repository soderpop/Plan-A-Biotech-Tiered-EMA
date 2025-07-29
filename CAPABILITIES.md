# Plan A Biotech MVP Capabilities

This document summarizes the functional capabilities demonstrated by the Tiered-EMA™ positional index implementation. The goal is to match the behaviour described in the pitch deck.

## Core Features

- **Constant Memory Footprint**: Uses exactly `8(K+1)` bytes regardless of stream length.
- **Multi-Tier EMA Updates**: Processes events across `K` tiers with `O(K)` computational complexity.
- **Bias Correction**: Provides bias-corrected position estimates for each tier.
- **Closed-Form Solution**: Includes a closed-form formula to compute any tier value at position `n` without iteration.
- **Precision Scaling**: Higher tiers offer exponentially finer accuracy.
- **Stream Agnostic**: Works for arbitrarily long streams without additional memory.

## Demonstration Script

`plan_a_mvp.py` exercises these features by processing a user-specified number of events and printing a table for the first few tiers:

```bash
python3 plan_a_mvp.py --events 50000 --tiers 20
```

The output shows raw EMA values, bias-corrected estimates and closed-form results so that the behaviour matches the pitch deck demonstration.
