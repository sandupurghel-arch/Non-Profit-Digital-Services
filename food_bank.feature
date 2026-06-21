Feature: Food Bank Stock Management
  As a food bank administrator
  I want to manage food stock levels accurately
  So that I can efficiently serve beneficiaries and avoid waste

  Background:
    Given the food bank stock system is active

  Scenario: Adding new stock items (Normal case)
    When a staff member adds 10 units of "soup" to stock
    Then the stock level for "soup" should be 10

  Scenario: Allocating items to a beneficiary (Normal case)
    Given the stock for "rice" is 20 units
    When 5 units of "rice" are allocated to a beneficiary
    Then the remaining stock for "rice" should be 15

  Scenario: Attempting to allocate more than available stock (Edge case)
    Given the stock for "pasta" is 3 units
    When 10 units of "pasta" are requested by a beneficiary
    Then the system should reject the allocation
    And an error message "Insufficient stock available" should be raised
