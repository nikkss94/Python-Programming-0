n = input("Enter a number: ")
n = int(n)

k = 2
is_prime = True 

if n == 1:
    is_prime = False

while k < n:
    if n % k == 0:
        is_prime = False
        break
    k = k + 1

if is_prime:
    print("It is prime")

else:
    print("It is not prime")
    
        
        
