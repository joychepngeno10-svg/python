def calculator():
    try:
        a = float(input("first number"))
        op = input("Operator (+,-,*,/):")
        b = float(input("second number:"))
    except ValueError:
        print("that wasn't a number.")
        return
    if op == "+":
        print("result", a+b)
    elif op == "-":
        print("result", a-b)
    elif op == "*":
        print("result", a*b)
    elif op == "/":
        if b == 0:
            print("division by zero is not allowed")
        else:
            print("result", a/b)
    else:
        print("invalid operator")
