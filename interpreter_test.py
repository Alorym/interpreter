from interpreter import Interpreter
def test_addition():
    interpreter = Interpreter('3+4')
    result = interpreter.expr()
    assert result == 7
def test_whitespace():
    interpreter = Interpreter('3 + 5')
    result = interpreter.expr()
    assert result == 8
def test_subtraction():
    interpreter = Interpreter('7-2')
    result = interpreter.expr()
    assert result == 5
def test_multicharintegers():
    interpreter = Interpreter('1400+4325')
    result = interpreter.expr()
    assert result == 5725
def test_multiplication():
    interpreter = Interpreter('60*2')
    result = interpreter.expr()
    assert result == 120
def test_divison():
    interpreter = Interpreter('30/2')
    result = interpreter.expr()
    assert result == 15.0