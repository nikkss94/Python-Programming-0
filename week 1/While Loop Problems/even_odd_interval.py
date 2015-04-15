a = input("Enter a: ")
a = int(a)
b = input("Enter b: ")
b = int(b)

while a <= b:
    n = a
    if n % 2 == 0:
        print(n, " - even")
    else:
        print(n," - odd")
    a = a + 1
