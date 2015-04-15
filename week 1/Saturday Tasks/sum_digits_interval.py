N = input("Enter N: ")
M = input("Enter M: ")
N = int(N)
M = int(M)
start = N

end = M
while start <= end:
    n = start
    sum = 0
    while n != 0:
        k = n % 10
        sum = sum + k
        n = n // 10
    
    print("Sum of digits of", start," = ", sum)
    start += 1
    

