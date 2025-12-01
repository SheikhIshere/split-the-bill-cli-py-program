# contribution-splitter

Simple CLI tool to collect member contributions, compute total expense, and calculate per-head balances so you know who owes or who gets refunded.

## What it is
A minimal, dependency-free Python script that:
- accepts member names and contribution amounts,
- validates input (non-empty names, non-negative integers, minimum member count),
- computes total, per-head share (rounded), and each member's balance,
- prints a readable summary showing who will receive or pay.

## Use cases
- Splitting group expenses (trips, events, dinners)
- Quick bookkeeping for small teams or friend groups
- Teaching/example script for basic CLI input validation and aggregation

## Quick start
```bash
# requires Python 3.8+
python main.py #for windows
python3 main.py #for linux

Follow the interactive prompts:

Enter total members (must be > 2)

For each member: enter name and contribution amount

Example output
===== Contribution Summary =====

✅ Alice      | Paid:      1000 | Per head:       750 | Will receive:      250
❌ Bob        | Paid:       500 | Per head:       750 | Will pay:          250

Notes & improvements

Currently accepts integer contributions only. Use int() parsing; change to float() if decimals/currency required.

Consider adding CSV import/export, CLI flags (argparse), and unit tests for production use.

Numbers can be formatted with thousands separators: f"{num:,}" for readability.

License

MIT


Want me to produce the actual `README.md` file content in a downloadable form or a ready-to-paste commit message you can use?
