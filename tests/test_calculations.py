import pytest
from app.calculation.calculation import Calculation
from app.calculation.factory import CalculationFactory
from app.operation.operations import Add, Subtract

# Use Add and Subtract classes from the operations module
operation_add = Add()
operation_subtract = Subtract()

# Parameterized test data: (a, b, operation, expected_result)
@pytest.mark.parametrize("a, b, operation, expected", [
    (5, 3, operation_add, 8),
    (10, 2, operation_subtract, 8),
    (1.5, 0.5, operation_add, 2.0),
])
def test_calculation_perform(a, b, operation, expected):
    """Test the perform method of the Calculation class."""
    calc = Calculation(a, b, operation)
    assert calc.perform() == expected

def test_calculation_create_classmethod():
    """Test the alternative create constructor."""
    calc = Calculation.create(1, 2, operation_add)
    assert calc.operand_a == 1
    assert calc.operand_b == 2
    assert calc.operation is operation_add

# Parameterized test data: (a, b, symbol, expected_result)
@pytest.mark.parametrize("a, b, symbol, expected", [
    (4, 2, '+', 6),
    (10, 5, '-', 5),
    (3, 4, '*', 12),
    (9, 3, '/', 3.0),
])
def test_calculation_factory_success(a, b, symbol, expected):
    """Test successful creation and execution via the CalculationFactory."""
    calc = CalculationFactory.create_calculation(a, b, symbol)
    assert isinstance(calc, Calculation)
    assert calc.perform() == expected

def test_calculation_factory_unknown_operation():
    """Test factory handling of an unknown operation symbol."""
    with pytest.raises(ValueError, match="Unknown operation: %"):
        CalculationFactory.create_calculation(1, 1, '%')