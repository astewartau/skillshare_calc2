
# main.py
# This is a feature branch comment

import argparse

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Division by zero is not allowed!"
        return a / b

    def factorial(self, a):
        if a < 0:
            return "Factorial of negative numbers is not allowed!"
        elif a == 0:
            return 1
        else:
            return a * self.factorial(a - 1)

    def modulus(self, a, b):
        if b == 0:
            return "Modulus by zero is not allowed!"
        return a % b

def main():
    parser = argparse.ArgumentParser(description="Perform arithmetic operations.")
    parser.add_argument("operation", type=str, choices=["add", "subtract", "multiply", "divide", "modulus", "factorial"],
                        help="The arithmetic operation to perform.")
    parser.add_argument("a", type=float, help="First number")
    parser.add_argument("b", type=float, help="Second number")

    args = parser.parse_args()

    calc = Calculator()

    if args.operation == "add":
        result = calc.add(args.a, args.b)
    elif args.operation == "subtract":
        result = calc.subtract(args.a, args.b)
    elif args.operation == "multiply":
        result = calc.multiply(args.a, args.b)
    elif args.operation == "divide":
        result = calc.divide(args.a, args.b)
    elif args.operation == "modulus":
        result = calc.modulus(args.a, args.b)
    elif args.operation == "factorial":
        result = calc.factorial(args.a)

    print(f"Result (main branch): {args.a} {args.operation} {args.b} = {result}")

if __name__ == "__main__":
    main()
