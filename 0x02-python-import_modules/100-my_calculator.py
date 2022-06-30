#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    total = len(argv)
    num1 = int(argv[1])
    num2 = int(argv[3])
    op = argv[2]
    if total != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
    else:
        if op != "+" or "-" or "*" or "/":
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            if op == "+":
                print("{} + {} = {}".format(num1, num2, add(num1, num2)))
                exit(0)
            elif op == "-":
                print("{} - {} = {}".format(num1, num2, sub(num1, num2)))
                exit(0)
            elif op == "*":
                print("{} * {} = {}".format(num1, num2, mul(num1, num2)))
                exit(0)
            elif op == "/":
                print("{} / {} = {}".format(num1, num2, div(num1, num2)))
                exit(0)
