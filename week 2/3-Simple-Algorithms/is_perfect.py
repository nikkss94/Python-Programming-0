n = input("Enter n: ")
n = int(n)

counter = 1
sum = 0

while counter < n:
    if n % counter == 0:
        sum = sum + counter
    counter += 1

if sum == n:
    print("The number is perfect!")

else:
    print("The number is not perfect!")
