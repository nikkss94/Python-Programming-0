n = input("Enter a number: ")
n = int(n)

number = 0
number_1 = n
while n != 0:
    k = n % 10
    number = number * 10 + k
    n = n // 10

if number == number_1:
    print("The number is palindrom")

if number != number_1:
    print("The number is not palindrom")
    
