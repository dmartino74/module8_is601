import pytest
from typing import Union
from app.operations import add, subtract, multiply, divide

Number = Union[int, float]

# -------------------------------
# Unit Tests for 'add' Function
# -------------------------------
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (-2, -3, -5),
        (2.5, 3.5, 6.0),
        (-2.5, 3.5, 1.0),
        (0, 0, 0),
        (1e10, 1e10, 2e10),  # Large numbers
        (1e-10, 1e-10, 2e-10),  # Small numbers
    ],
    ids=[
        "add_two_positive_integers",
        "add_two_negative_integers",
        "add_two_positive_floats",
        "add_negative_and_positive_float",
        "add_zeros",
        "add_large_numbers",
        "add_small_numbers",
    ]
)
def test_add(a: Number, b: Number, expected: Number):
    result = add(a, b)
    assert result == expected

# -------------------------------
# Unit Tests for 'subtract'
# -------------------------------
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 2),
        (-5, -3, -2),
        (5.5, 2.5, 3.0),
        (-5.5, -2.5, -3.0),
        (0, 0, 0),
    ]
)
def test_subtract(a: Number, b: Number, expected: Number):
    result = subtract(a, b)
    assert result == expected

# -------------------------------
# Unit Tests for 'multiply'
# -------------------------------
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),
        (-2, 3, -6),
        (2.5, 4.0, 10.0),
        (-2.5, 4.0, -10.0),
        (0, 5, 0),
    ]
)
def test_multiply(a: Number, b: Number, expected: Number):
    result = multiply(a, b)
    assert result == expected

# -------------------------------
# Unit Tests for 'divide'
# -------------------------------
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 3, 2.0),
        (-6, 3, -2.0),
        (6.0, 3.0, 2.0),
        (-6.0, 3.0, -2.0),
        (0, 5, 0.0),
    ]
)
def test_divide(a: Number, b: Number, expected: float):
    result = divide(a, b)
    assert result == expected

# -------------------------------
# Negative Test: Division by Zero
# -------------------------------
def test_divide_by_zero():
    with pytest.raises(ValueError) as excinfo:
        divide(6, 0)
    assert "Cannot divide by zero!" in str(excinfo.value)

# -------------------------------
# Optional: Type Error Handling
# -------------------------------
@pytest.mark.parametrize("a, b", [("a", 5), (None, 3)])
def test_add_invalid_types(a, b):
    with pytest.raises(TypeError):
        add(a, b)
