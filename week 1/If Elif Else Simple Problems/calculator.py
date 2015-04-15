a = input("Enter a: ")
b = input("Enter b: ")
a = int(a)
b = int(b)

oper = input("Enter operation: ")
if oper == '+':
    print("Result is:")
    print(a + b)
elif oper == '-':
    print("Result is:")
    print(a - b)
elif oper == '*':
    print("Result is:")
    print(a * b)
if oper == '/':
    print("Result is:")
    print(a / b)
if oper != "+" and oper != "-" and oper != "*" and oper != "/":
    print("We do not support that operation.")
