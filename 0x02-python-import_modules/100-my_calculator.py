#!/usr/bin/python3
import sys
from calculator_1 import add, mul, sub, div

if __name__ == "__main__":
    args = sys.argv
    if (len(args)) != 4:
        print("./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        if (args[2] != '*' and args[2] != '+' and
                args[2] != '-' and args[2] != '/'):
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        else:
            a = int(args[1])
            b = int(args[3])
            math = 0
            if args[2] == '+':
                math = add(a, b)
            elif args[2] == '-':
                math = sub(a, b)
            elif args[2] == '*':
                math = mul(a, b)
            else:
                math = div(a, b)
            print("{} {} {} = {}".format(a, args[2], b, math))
