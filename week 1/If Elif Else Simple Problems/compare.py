a = input("Enter a: ")
b = input("Enter b: ")
a = int(a)
b = int(b)

if a > b:
    print("a(",a,") is bigger than b(",b,")!")
elif a == b:
    print("a(",a,") is equal to b(",b,")")
else:
    print("b(",b,") is bigger than a(",a,")")
