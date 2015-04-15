n = input("Enter a 3-digit number: ")
n = int(n)

a = n % 10
n = n // 10
b = n % 10
n = n // 10
c = n

if a >= b and a >= c:
    largest_digit = a

if b >= a and b >= c:
    largest_digit = b

if c >= a and c >= b:
    largest_digit = c

print("The largest digit is ", largest_digit)


if a <= b and a <= c:
    smallest_digit = a

if b <= a and b <= c:
    smallest_digit = b

if c <= a and c <= b:
    smallest_digit = c

print("The smallest digit is ", smallest_digit)

middle_digit = a

if (largest_digit == a and smallest_digit == b) or (largest_digit == b and smallest_digit == a):
    middle_digit = c

if (largest_digit == a and smallest_digit == c) or (largest_digit == c and smallest_digit == a):
    middle_digit = b

print ("The middle digit is ", middle_digit)

biggest_number = 100 * largest_digit + 10 * middle_digit + smallest_digit
smallest_number = 100 * smallest_digit + 10 * middle_digit + largest_digit

print("The biggest number is ", biggest_number)
print("The smallest number is ", smallest_number)









