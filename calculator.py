def multiply(a, b):
    return a * b

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python calculator.py <number1> <number2>")
    else:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        result = multiply(num1, num2)
        print("Multiplication result:", result)
