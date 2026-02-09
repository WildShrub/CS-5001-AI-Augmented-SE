import cmath

def convert(numbers):
    """Convert a complex number to its polar form.

    Args:
        numbers: A complex number or a sequence of complex numbers.

    Returns:
        A tuple (magnitude, phase) for a single complex number,
        or a list of such tuples for a sequence of complex numbers.
    """
    return cmath.polar(numbers)
