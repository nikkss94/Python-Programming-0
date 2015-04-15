n = input("Enter n: ")
n = int(n)

numbers = []

while n != 0:
    k = n % 10
    numbers = numbers + [k] 
    n = n // 10

f = False

for number in numbers:
 if number in [2,3,5,7]:
    f = True
    break


if f:
    print("yes")
else :
    print("no")
