def add(a, b) -> int:
    """
    Adds two numbers (test).
    """
    return a + b

def subtract(a, b):
    """
    Subtracts two numbers.

    :param kind: two numbers to be subtracted.
    :type kind: float, float
    :raise calculator.IncompatibleTypes: If the kind is invalid.
    :return: subtraction of two numbers.
    :rtype: float
    """
    return a - b

def multiply(a, b):
    """
    Multiplies two numbers.

    :param kind: two numbers to be multiplied.
    :type kind: float, float
    :raise calculator.IncompatibleTypes: If the kind is invalid.
    :return: multiplication of two numbers.
    :rtype: float
    """
    return a * b

def divide(a, b):
    """
    Divides two numbers.

    :param kind: two numbers to be divided.
    :type kind: float, float
    :raise calculator.IncompatibleTypes: If the kind is invalid.
    :return: division of two numbers.
    :rtype: float
    """
    return a / b

class IncompatibleTypes(Exception):
    """Raised if the two operands are incompatible."""
    pass