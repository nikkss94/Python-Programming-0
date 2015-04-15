n = input("Enter n: ")
n = int(n)

counter = 0
names = []

while counter < n:
    name = input("")
    names = names + [name]
    counter += 1

names = sorted(names)
print("Sorted names are: ")

for name in names:
    print(name)
    
