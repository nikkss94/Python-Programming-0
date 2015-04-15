n = input("Enter some number: ")
n = int(n)

while n != 0:
    k = n % 10
    print(k)
    n = n // 10
    
