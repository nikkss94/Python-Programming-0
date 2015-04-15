n = input("Enter n: ")
n = int(n)
k = 1
sum = 0
while k <= n:
    if k % 2 == 0:
        sum = sum + k
    k = k + 1
print(sum)
