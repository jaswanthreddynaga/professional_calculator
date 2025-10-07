import pytest
from app.operation.operations import Add, Subtract, Multiply, Divide

# Parameterized test data: (a, b, expected_result)
@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 8),
    (-1, 1, 0),
    (0.5, 0.5, 1.0),
])
def test_add_operation(a, b, expected):
    """Test addition operation."""
    assert Add().calculate(a, b) == expected

# Parameterized test data: (a, b, expected_result)
@pytest.mark.parametrize("a, b, expected", [
    (10, 4, 6),
    (5, 5, 0),
    (0, 10, -10),
])
def test_subtract_operation(a, b, expected):
    """Test subtraction operation."""
    assert Subtract().calculate(a, b) == expected

# Parameterized test data: (a, b, expected_result)
@pytest.mark.parametrize("a, b, expected", [
    (2, 4, 8),
    (-2, 3, -6),
    (1.5, 2, 3.0),
])
def test_multiply_operation(a, b, expected):
    """Test multiplication operation."""
    assert Multiply().calculate(a, b) == expected

# Parameterized test data: (a, b, expected_result)
@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5.0),
    (-8, 4, -2.0),
    (1, 3, 1/3),
])
def test_divide_operation_success(a, b, expected):
    """Test successful division operation."""
    assert Divide().calculate(a, b) == expected

def test_divide_operation_by_zero():
    """Test division by zero error handling."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Divide().calculate(10, 0)