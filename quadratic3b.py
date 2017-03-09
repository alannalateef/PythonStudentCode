# quadratic3b.py
# Using if-else to avoid program crash
import math
def main():
    print("Find the real solutions to a quadratic.")
    a, b, c = eval(input("Enter the coefs (a, b, c):"))
    discrim = b * b - 4 * a * c
    if discrim < 0:
        print("The equation has no real roots!")
    else:
        if discrim == 0:
            root = - b / (2 * a)
            print("There is a double root:", root)
        else:
            discRoot = math.sqrt(b * b - 4 * a * c)
            root1 = (-b + discRoot) / (2 * a)
            root2 = (-b - discRoot) / (2 * a)
            print("The solutions are:", root1, root2)
main()
