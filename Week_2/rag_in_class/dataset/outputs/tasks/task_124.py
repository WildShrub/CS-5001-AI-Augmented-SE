import cmath

def angle_complex(a, b):
    complex_number = complex(a, b)
    angle = cmath.phase(complex_number)
    return angle
