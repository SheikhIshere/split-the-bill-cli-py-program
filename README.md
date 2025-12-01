# contribution-splitter

CLI tool to split group expenses, calculate per-head share, and track who owes or gets refunded.

## Description

Minimal Python script:

* Collects member names and contributions.
* Validates input (non-empty, non-negative, min 3 members).
* Computes total, per-head, and balances.
* Prints clear summary of who will pay or receive.

## Use Cases

* Trips, events, dinners, small team expenses.
* Quick bookkeeping.
* Learning example for CLI input validation and aggregation.

## Quick Start

```bash
python main.py        # Windows
python3 main.py       # Linux
```

Follow prompts for member count, names, and contributions.

Example output:

```
===== Contribution Summary =====
✅ Alice      | Paid:      1000 | Per head:       750 | Will receive:      250
❌ Bob        | Paid:       500 | Per head:       750 | Will pay:          250
```
