"""
bdd_runner.py — Standalone BDD-style runner for the Food Bank Stock system.

This reproduces the human-readable scenario report shown in Appendix A.4
without requiring the `behave` package. It exercises the same FoodBankStock
class through the same Given-When-Then steps described in food_bank.feature.
"""

from food_bank import FoodBankStock

LINE = "-" * 60


def run():
    print("Feature: Food Bank Stock Management")
    print("  As a food bank administrator")
    print("  I want to manage food stock levels accurately")
    print("  So that I can efficiently serve beneficiaries and avoid waste")
    print()

    passed = 0
    total = 0

    # Scenario 1 — Normal case
    total += 1
    print('  Scenario: Adding new stock items (Normal case)')
    print('    Given the food bank stock system is active')
    print('    When  a staff member adds 10 units of "soup" to stock')
    print('    Then  the stock level for "soup" should be 10')
    system = FoodBankStock()
    assert system.is_active()
    system.add_stock("soup", 10)
    assert system.get_stock("soup") == 10
    print("  PASSED  All steps passed")
    print()
    passed += 1

    # Scenario 2 — Normal case
    total += 1
    print('  Scenario: Allocating items to a beneficiary (Normal case)')
    print('    Given the food bank stock system is active')
    print('    And   the stock for "rice" is 20 units')
    print('    When  5 units of "rice" are allocated to a beneficiary')
    print('    Then  the remaining stock for "rice" should be 15')
    system = FoodBankStock()
    system.add_stock("rice", 20)
    system.allocate_to_beneficiary("rice", 5)
    assert system.get_stock("rice") == 15
    print("  PASSED  All steps passed")
    print()
    passed += 1

    # Scenario 3 — Edge case
    total += 1
    print('  Scenario: Attempting to allocate more than available (Edge case)')
    print('    Given the food bank stock system is active')
    print('    And   the stock for "pasta" is 3 units')
    print('    When  10 units of "pasta" are requested by a beneficiary')
    print('    Then  the system should reject the allocation')
    print('    And   error message "Insufficient stock available" should be raised')
    system = FoodBankStock()
    system.add_stock("pasta", 3)
    error = None
    try:
        system.allocate_to_beneficiary("pasta", 10)
    except ValueError as exc:
        error = str(exc)
    assert error is not None
    assert error == "Insufficient stock available"
    print("  PASSED  All steps passed")
    print()
    passed += 1

    print(LINE)
    print(f"{total} scenarios ({passed} passed)")
    print(LINE)


if __name__ == "__main__":
    run()
