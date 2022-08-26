from behave import *
from distutils.util import strtobool
from net.mobiustesseract.truetest import TrueTest


@when('a \'{parameter}\' is entered')
def step_impl(context, parameter):
    parameter = strtobool(parameter)
    context.result = TrueTest().negate(parameter)

@then('the result should be the negation of the \'{parameter}\'')
def step_impl(context, parameter):
    parameter = strtobool(parameter)
    assert (not parameter) == context.result
