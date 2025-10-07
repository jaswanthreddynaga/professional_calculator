"""
Defines the base Calculation class.
"""

class Calculation:
    """Represents a single calculation instance."""
    def __init__(self, operand_a, operand_b, operation):
        self.operand_a = operand_a
        self.operand_b = operand_b
        self.operation = operation

    @classmethod
    def create(cls, operand_a, operand_b, operation):
        """Alternative constructor."""
        return cls(operand_a, operand_b, operation)

    def perform(self):
        """Executes the calculation."""
        return self.operation.calculate(self.operand_a, self.operand_b)

    def __str__(self):
        """String representation for history."""
        # Simple string representation; you might enhance this.
        op_symbol = getattr(self.operation, 'symbol', '?')
        return f"{self.operand_a} {op_symbol} {self.operand_b} = {self.perform()}"