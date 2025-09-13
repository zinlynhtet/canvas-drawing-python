from math import gcd

class Fraction:
    """Class representing a fraction a/b in reduced form."""
    
    def __init__(self, a, b):
        """Initialize fraction and reduce it."""
        if b == 0:
            raise ValueError("Denominator cannot be zero")
        # Ensure denominator is positive
        if b < 0:
            a = -a
            b = -b
        g = gcd(a, b)
        self.num = a // g
        self.den = b // g

    def __str__(self):
        """Return string representation in a/b form."""
        return f"{self.num}/{self.den}"

    def __eq__(self, other):
        """Check if two fractions are equal."""
        return self.num == other.num and self.den == other.den

    def __add__(self, other):
        """Add two fractions."""
        num = self.num * other.den + self.den * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __sub__(self, other):
        """Subtract two fractions."""
        num = self.num * other.den - self.den * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __mul__(self, other):
        """Multiply two fractions."""
        num = self.num * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __truediv__(self, other):
        """Divide two fractions."""
        if other.num == 0:
            raise ZeroDivisionError("Cannot divide by zero fraction")
        num = self.num * other.den
        den = self.den * other.num
        return Fraction(num, den)


# Read fractions p, q, r
p = Fraction(int(input()), int(input()))
q = Fraction(int(input()), int(input()))
r = Fraction(int(input()), int(input()))

# Compute (p/q)*(p+q) - q
s = (p / q) * (p + q) - q

# Print results
print(s)
print(s == r)
