n = input("Enter n: ")
n = int(n)

counter = 1

while counter < n:
    if n % counter == 0:
        print(n," % ",counter, " == 0")
    counter += 1
