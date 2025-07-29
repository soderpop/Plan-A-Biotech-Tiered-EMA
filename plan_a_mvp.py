"""Plan A Biotech MVP using Tiered-EMA positional index.

This script mirrors the simple demonstration shown in the pitch deck.  It
processes a stream of events using the :class:`TieredEMA` class and prints
memory usage plus the position estimates from the first few tiers.  For each
tier we display the raw EMA value, the bias-corrected estimate and the
closed-form solution used in the deck.  This confirms the constant-memory and
closed‑form properties of the algorithm.
"""

import argparse
from tiered_ema import TieredEMA


def run_simulation(num_events: int, num_tiers: int) -> None:
    """Process ``num_events`` updates and display tier estimates."""

    ema = TieredEMA(num_tiers)

    for i in range(1, num_events + 1):
        ema.update(i)

    print(f"Processed {num_events:,} events with {num_tiers} tiers.")
    print(f"Constant memory usage: {ema.get_memory_usage()} bytes")
    print()

    headers = ["Tier", "Raw EMA", "Bias Corrected", "Closed Form", "Δ Closed"]
    rows = []

    for k in range(min(5, num_tiers)):
        raw = ema.get_position(k)
        corrected = ema.get_corrected_position(k)
        closed = ema.get_closed_form_position(k, num_events)
        diff = abs(raw - closed)
        rows.append(
            [
                k,
                f"{raw:.6f}",
                f"{corrected:.6f}",
                f"{closed:.6f}",
                f"{diff:.6e}",
            ]
        )

    from tabulate import tabulate

    print(tabulate(rows, headers=headers, tablefmt="github"))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Plan A Biotech MVP using the Tiered-EMA positional index"
    )
    parser.add_argument(
        "--events",
        type=int,
        default=10000,
        help="Number of events to simulate",
    )
    parser.add_argument(
        "--tiers",
        type=int,
        default=20,
        help="Number of EMA tiers to use",
    )
    args = parser.parse_args()

    run_simulation(args.events, args.tiers)


if __name__ == "__main__":
    main()
