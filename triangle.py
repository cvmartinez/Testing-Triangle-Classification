import math


def classify_triangle(a: float, b: float, c: float) -> str:


    # Validate input (all sides should be positive)
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid input"

    # Sort sides for easier right-triangle checking
    sides = sorted([a, b, c])
    x, y, z = sides  # x and y are the shortest, z is the longest

    # Check if it's a valid triangle
    if x + y <= z:
        return "Not a triangle"

    # Determine triangle type
    if a == b == c:
        triangle_type = "Equilateral"
    elif a == b or b == c or a == c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"

    # Check for right triangle using Pythagorean theorem (Used AI)
    if math.isclose(x ** 2 + y ** 2, z ** 2, rel_tol=1e-9):
        triangle_type += " and Right"

    return triangle_type