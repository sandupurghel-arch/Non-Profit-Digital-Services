# Food Bank Stock Management — BDD Prototype (SWE6301 Assessment 1, Task 2)

A Behaviour-Driven Development (BDD) prototype modelling a food bank stock
management service for a non-profit organisation.

## Project structure

```
food_bank_bdd/
├── food_bank.py                      # Core FoodBankStock class
├── food_bank.feature                 # Gherkin scenarios (reference copy)
├── bdd_runner.py                     # Standalone runner (no dependencies)
├── requirements.txt
└── features/
    ├── food_bank.feature             # Feature file used by `behave`
    └── steps/
        └── food_bank_steps.py        # Given-When-Then step definitions
```

## Running the tests

### Option 1 — standalone runner (no install needed)

```bash
python3 bdd_runner.py
```

### Option 2 — with the behave framework

```bash
pip install -r requirements.txt
behave
```

Both run the same three scenarios: two normal cases and one edge case
(insufficient stock), all of which pass.
