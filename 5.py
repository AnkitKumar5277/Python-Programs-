# The standard form of a quadratic equation is:
# ax2 + bx + c = 0, where
# a, b and c are real numbers and
# a ≠ 0

# The solutions of this quadratic equation is given by:
# (-b ± (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
import cmath
a = 1
b = 5
c = 6
# calculate the discriminant
d = (b**2) - (4*a*c)
# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print('The solution are {0} and {1}'.format(sol1,sol2))

# Enter a: 1
# Enter b: 5
# Enter c: 6
# The solutions are (-3+0j) and (-2+0j)

# challenge
import cmath  # For handling complex numbers
def solve_quadratic(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    # Calculate the two solutions using the quadratic formula
    root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    # Return the roots as a list, ensuring root1 appears first
    return [root1, root2]
