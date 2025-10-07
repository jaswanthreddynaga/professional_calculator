"""
Defines classes for basic arithmetic operations.
"""

class Operation:
    """Base class for all operations."""
    def calculate(self, a, b):
        """Perform the operation."""
        raise NotImplementedError("Subclasses must implement the calculate method.")

class Add(Operation):
    """Addition operation."""
    def calculate(self, a, b):
        return a + b

class Subtract(Operation):
    """Subtraction operation."""
    def calculate(self, a, b):
        return a - b

class Multiply(Operation):
    """Multiplication operation."""
    def calculate(self, a, b):
        return a * b

class Divide(Operation):
    """Division operation with error handling."""
    def calculate(self, a, b):
        # EAFP (Easier to Ask Forgiveness than Permission) for error handling
        try:
            return a / b
        except ZeroDivisionError:
            raise ValueError("Error: Cannot divide by zero.")