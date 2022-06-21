def add(a, b):
    """
    Adds two numbers.

    :param kind: two numbers to be added.
    :type kind: float, float.
    :raise calculator.IncompatibleTypes: If the kind is invalid.
    :return: sum of two numbers.
    :rtype: float
    """
    return a + b

def subtract(a, b):
    """
    Subtracts two numbers.

    :param kind: two numbers to be added.
    :type kind: float, float.
    :raise calculator.IncompatibleTypes: If the kind is invalid.
    :return: sum of two numbers.
    :rtype: float
    """
    return a - b

def multiply(a, b):
    """
    Adds two numbers.

    :param kind: two numbers to be added.
    :type kind: float, float.
    :raise calculator.IncompatibleTypes: If the kind is invalid.
    :return: sum of two numbers.
    :rtype: float
    """
    return a * b

def divide(a, b):
    """
    Adds two numbers.

    :param kind: two numbers to be added.
    :type kind: float, float.
    :raise calculator.IncompatibleTypes: If the kind is invalid.
    :return: sum of two numbers.
    :rtype: float
    """
    return a + b

class IncompatibleTypes(Exception):
    """Raised if the two operands are incompatible."""
    pass