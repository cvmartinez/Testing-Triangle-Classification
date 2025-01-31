import pytest
from triangle import classify_triangle

def test_equilateral():
    assert classify_triangle(5, 5, 5) == "Equilateral"

def test_isosceles():
    assert classify_triangle(5, 5, 3) == "Isosceles"
    assert classify_triangle(3, 5, 5) == "Isosceles"
    assert classify_triangle(5, 3, 5) == "Isosceles"



def test_scalene():
    assert classify_triangle(7, 10, 5) == "Scalene"

def test_right_triangle():
    assert classify_triangle(3, 4, 5) == "Scalene and Right"
    assert classify_triangle(5, 12, 13) == "Scalene and Right"
    assert classify_triangle(8, 15, 17) == "Scalene and Right"

def test_not_a_triangle():
    assert classify_triangle(1, 2, 3) == "Not a triangle"
    assert classify_triangle(10, 2, 3) == "Not a triangle"

def test_invalid_inputs():
    assert classify_triangle(-1, 4, 5) == "Invalid input"
    assert classify_triangle(0, 4, 5) == "Invalid input"
    assert classify_triangle(3, -4, 5) == "Invalid input"