"""
Defines the CalculationFactory for creating Calculation instances.
"""
from app.operation.operations import Add, Subtract, Multiply, Divide
from app.calculation.calculation import Calculation

class CalculationFactory:
    """Factory to create Calculation objects based on an operation string."""

    # Map of operation symbols to their respective classes
    OPERATIONS = {
        '+': Add,
        '-': Subtract,
        '*': Multiply,
        '/': Divide,
    }

    @staticmethod
    def create_calculation(operand_a, operand_b, operation_symbol):
        """
        Creates a Calculation instance.

        :param operand_a: First number.
        :param operand_b: Second number.
        :param operation_symbol: The symbol (+, -, *, /) for the operation.
        :return: A Calculation instance.
        :raises ValueError: If the operation symbol is not recognized.
        """
        operation_class = CalculationFactory.OPERATIONS.get(operation_symbol)

        if operation_class:
            # Instantiate the operation object
            operation_instance = operation_class()
            # Create and return the Calculation object
            return Calculation.create(operand_a, operand_b, operation_instance)
        else:
            raise ValueError(f"Unknown operation: {operation_symbol}. Use one of: {list(CalculationFactory.OPERATIONS.keys())}")