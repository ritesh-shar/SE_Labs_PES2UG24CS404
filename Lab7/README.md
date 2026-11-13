# Lab 7 – Fuzz Testing

## Overview

This lab demonstrates fuzz testing using Python's Hypothesis library.

The objective is to identify input validation bugs in a tennis scoring application, fix the issues, and verify the improvements using automated tests.

## Project Structure

```text
lab7/
│
├── tennis_scoring.py
├── test_tennis_scoring.py
└── README.md
```

## Functions Tested

| Function | Description |
|---|---|
| `parse_score()` | Parses tennis scores in A-B format |
| `game_lead()` | Calculates the difference between tennis point values |
| `set_spread()` | Calculates the spread between game scores |

## Requirements

- Python 3.8+
- Hypothesis
- Pytest

## Installation

Install the required dependencies:

```bash
python -m pip install hypothesis pytest
```

## Execution

Run the application:

```bash
python tennis_scoring.py
```

Run the fuzz tests:

```bash
python -m pytest test_tennis_scoring.py -v
```

## Testing Methodology

Hypothesis was used to generate random strings and None values to test all three application functions.

The initial implementation produced failures when unexpected inputs were supplied.

The application was subsequently modified to include:

- Input type validation
- Input format validation
- Numeric validation
- Negative value checks
- Exception handling

## Results

| Testing Stage | Result |
|---|---|
| Original application | Successful with valid inputs |
| Initial fuzz testing | 3 tests failed |
| Fixed application | Successful with valid inputs |
| Final test execution | 6 tests passed |

## Conclusion

Fuzz testing helped identify input validation weaknesses in the original application. After implementing defensive programming and input validation, all six automated tests passed successfully.

## Technologies Used

Python · Hypothesis · Pytest
