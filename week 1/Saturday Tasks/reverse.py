number = input()
number = int(number)
new_number = 0

while number != 0:
    k = number % 10
    new_number = new_number * 10 + k
    number = number // 10
print (new_number)
