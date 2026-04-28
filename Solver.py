import cmath

def solve_quadratic(a, b, c):
    # Check if it's actually a quadratic equation
    if a == 0:
        if b == 0:
            return None  # No solution or infinite solutions
        return -c / b, None
        
    # Calculate the discriminant
    d = (b**2) - (4*a*c)
    
    # Calculate two solutions
    x1 = (-b - cmath.sqrt(d)) / (2*a)
    x2 = (-b + cmath.sqrt(d)) / (2*a)
    
    return x1, x2

# Coefficients
a, b, c = 6, -4, 3

print(f"Equation: {a}x² + {b}x + {c} = 0")
roots = solve_quadratic(a, b, c)

if roots:
    print(f"x1 = {roots[0]}")
    print(f"x2 = {roots[1]}")
    
