from behave import when, then, given
from calculadora import Calculadora

@given(u'o inteiro real {value:d}')
def given_a_value(context, value):
    print(value)
    context.a = value
    pass

@when(u'eu somo 3 com {value:d}')
def when_b_value(context, value):
    print(value)
    context.b = value
    pass

@then(u'o resultado é {value:d}')
def then_soma_deve_ser_igual(context,value):
    print(value)
    assert Calculadora.soma(a=context.a, b=context.b) == value