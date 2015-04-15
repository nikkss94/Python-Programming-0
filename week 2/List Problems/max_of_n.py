n = input("Enter n: ")
n = int(n)
 
count = 0
numbers = []
 
while count < n:
    
    number = input("")
    number = int(number)
 
    numbers = numbers + [number]
    count += 1
 
max_number = numbers[0] 
 
for number in numbers:
    if max_number < number:
        max_number = number
 
print("Max is: ",max_number)