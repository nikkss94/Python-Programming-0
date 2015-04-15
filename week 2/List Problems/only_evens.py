n = input("Enter count: ")
n = int(n)

numbers = []
count = 1

while count <= n:
    k = input("Enter number: ")
    k = int(k)
    
    if k % 2 == 0:
        numbers = numbers + [k]
    count += 1  

print("Count of evens: ",len(numbers))
print("Evens are: ")

for even in numbers:
    print(even)
