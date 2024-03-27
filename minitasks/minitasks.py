import re

# Minitask 2
# Change the last "du" to "DU"
pattern = re.compile(r"\bdu(?!.*?\bdu\b)\b")
text = ["du du du", "du po ledu", "dopředu du", "i dozadu du", "dudu dupl", "Rammstein du hast"]
for row in text:
    print(re.sub(pattern, "DU", row))


# Minitask 3
# Define several mathematical functions and demonstrate their usage
def complex_func(x, y):
    """Calculate a complex function."""
    return 2 ** x ** y


def first(x):
    """Calculate the result of the first function."""
    return 2 ** x - 1


def second(x):
    """Calculate the result of the second function."""
    return 3 ** x - 2


def third(x):
    """Calculate the result of the third function."""
    return 5 ** x - 3


# List of functions first, second, third, complex_func
funlist = [first, second, third, complex_func]
a = 2
b = 3
# Print the result of the last function in the list with parameters a and b
print(funlist[-1](a, b))
# From the second to the third
for func in funlist[1:3]:
    # Print the result of the function with parameter a
    print(func(a))


# Minitask 6
# Define a class for representing 2D points and demonstrate its usage
class Point:
    """Represents a point in 2D space."""

    def __init__(self, x=0, y=0):
        """Initialize the Point object."""
        self.x = x
        self.y = y

    def __sub__(self, other):
        """Subtract two points."""
        return Point(self.x - other.x, self.y - other.y)

    def __str__(self):
        """Return a string representation of the Point object."""
        return f"Point({self.x}, {self.y})"


# Create instances of Point and demonstrate subtraction operation
p0 = Point()
p1 = Point(3, 4)
print(p0 - p1)
p2 = Point(1, 2)
result = p1 - p2
print(result)
