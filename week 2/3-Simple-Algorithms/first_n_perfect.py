n = input("Enter n: ")
n = int(n)
 
number = 6
 
 
while True:
    sum = 0
    counter = 1
    count = 1
 
    while counter < number:
        if number % counter == 0:
            sum += counter
 
        counter += 1
    if sum == number:
        print(number)
        count += 1
 
    if n == count:
        break
 
    number += 1
    
    
        
    
