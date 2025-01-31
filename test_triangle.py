import pytest  # Import pytest
from triangle import classify_triangle  # Import function from triangle.py

# Test for an equilateral triangle
def test_equilateral():
    assert classify_triangle(5, 5, 5) == "Equilateral"

# Test for an isosceles triangle
def test_isosceles():
    assert classify_triangle(5, 5, 3) == "Isosceles"

# Test for a scalene triangle
def test_scalene():
    assert classify_triangle(7, 10, 5) == "Scalene"

# Test for a right triangle
def test_right_triangle():
    assert classify_triangle(3, 4, 5) == "Scalene and Right"

# Test for invalid triangle
def test_not_a_triangle():
    assert classify_triangle(1, 2, 3) == "Not a triangle"

# Run tests if this file is executed directly (optional, but useful)
if __name__ == "__main__":
    pytest.main()