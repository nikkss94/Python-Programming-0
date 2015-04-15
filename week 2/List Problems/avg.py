n = input("Enter n: ")
n = int(n)

count = 0
sum = 0

while count < n:
    number = input("")
    number = int(number)
    sum = sum + number
    count += 1

print("Avg is ", sum / 2)
