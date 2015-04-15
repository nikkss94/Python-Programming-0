p = input("Enter p: ")
p = int(p)

q1 = p - 2
q2 = p + 2
counter = 2
count = 2
start = 2

while start < p:
    k = False
    if p % start == 0:
        break
    if p % start != 0:
        start += 1
        k = True
if k:        

    print("Twin primes with ",p," :")

    while counter < q1:
        p = False
        if q1 % counter == 0:
            print(q1," is not prime.")
            break
        if q1 % counter != 0:
            counter += 1
            p = True

    while count < q2:
        f = False
        if q2 % count == 0:
            print(q2," is not prime.")
            break
        if q2 % count != 0:
            count += 1
            f = True

    if f:  
        print(q2," is prime")
    if p:
        print(q1," is prime")
else:
    print(p," is not prime.")
