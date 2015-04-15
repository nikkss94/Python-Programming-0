n = input("Enter n: ")
n = int(n)
 
start = 0
numbers = []
 
while start < n:
    number = input("")
    number = int(number)
    numbers = numbers + [number]
    start += 1
min_number = numbers[0]
for number in numbers:
    if min_number > number:
        min_number = number
print("Min is: ",min_number)
