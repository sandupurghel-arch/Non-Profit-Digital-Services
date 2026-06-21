from behave import given, when, then
from food_bank import FoodBankStock


@given('the food bank stock system is active')
def step_system_active(context):
    context.system = FoodBankStock()
    context.error = None
    assert context.system.is_active()


@given('the stock for "{item}" is {quantity:d} units')
def step_set_stock(context, item, quantity):
    context.system.add_stock(item, quantity)


@when('a staff member adds {quantity:d} units of "{item}" to stock')
def step_add_stock(context, quantity, item):
    context.result = context.system.add_stock(item, quantity)


@when('{quantity:d} units of "{item}" are allocated to a beneficiary')
def step_allocate(context, quantity, item):
    context.result = context.system.allocate_to_beneficiary(item, quantity)


@when('{quantity:d} units of "{item}" are requested by a beneficiary')
def step_request(context, quantity, item):
    try:
        context.system.allocate_to_beneficiary(item, quantity)
        context.error = None
    except ValueError as exc:
        context.error = str(exc)


@then('the stock level for "{item}" should be {quantity:d}')
def step_check_stock(context, item, quantity):
    assert context.system.get_stock(item) == quantity


@then('the remaining stock for "{item}" should be {quantity:d}')
def step_check_remaining(context, item, quantity):
    assert context.system.get_stock(item) == quantity


@then('the system should reject the allocation')
def step_rejected(context):
    assert context.error is not None


@then('an error message "{expected}" should be raised')
def step_error_msg(context, expected):
    assert context.error == expected
