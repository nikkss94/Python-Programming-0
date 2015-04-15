n = input("Enter number n: ")
n = int(n)
 
sum = 0
numbers = []
 
while n != 0:
    number = n % 10
    numbers = [number] + numbers
    n = n // 10
 
print("List of digits is: ", numbers)
 
for number in numbers:
    sum = sum * 10 + number
print("Number is: ", sum)
