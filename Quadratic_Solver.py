import cmath
import datetime
import os

def solve_quadratic(a, b, c):
    """
    Calculates the roots of ax^2 + bx + c = 0.
    Handles linear cases (a=0) and complex roots.
    """
    if a == 0:
        if b == 0:
            return None  # Not an equation
        return (-c / b), None  # Linear equation (bx + c = 0)

    # Discriminant: D = b^2 - 4ac
    d = (b**2) - (4*a*c)

    # Quadratic Formula: x = (-b ± √D) / 2a
    root1 = (-b - cmath.sqrt(d)) / (2*a)
    root2 = (-b + cmath.sqrt(d)) / (2*a)

    return root1, root2

def save_result(a, b, c, roots):
    """Saves calculation history to a folder named 'samples'."""
    folder = "samples"
    
    # Agar folder nahi hai toh naya bana dega
    if not os.path.exists(folder):
        os.makedirs(folder)

    file_path = os.path.join(folder, "results.txt")
    
    with open(file_path, "a", encoding="utf-8") as f:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{now}] Equation: {a}x² + ({b})x + ({c}) = 0\n")
        f.write(f"Result: x1={roots[0]}, x2={roots[1]}\n")
        f.write("-" * 40 + "\n")

def main():
    print("========================================")
    print("   PRO QUADRATIC EQUATION SOLVER")
    print("========================================\n")
    
    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))

        roots = solve_quadratic(a, b, c)

        if roots is None:
            print("\n[!] Error: This is not a valid equation.")
        elif roots[1] is None:
            print(f"\n[i] Linear Equation Detected! Root x = {roots[0]:.2f}")
            save_result(a, b, c, roots)
        else:
            print(f"\n✅ Success! Roots for {a}x² + ({b})x + ({c}) = 0 are:")
            print(f"   x1 = {roots[0]}")
            print(f"   x2 = {roots[1]}")
            
            save_result(a, b, c, roots)
            print("\n[✔] Results logged in 'samples/results.txt'")

    except ValueError:
        print("\n[!] Error: Please enter numbers only (e.g., 5, -2, 3.5).")

if __name__ == "__main__":
    main()
                    
