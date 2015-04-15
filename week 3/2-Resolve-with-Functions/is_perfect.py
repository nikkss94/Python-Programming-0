def is_perfect(n):
    counter = 1
    sum = 0
 
    while counter < n:
        if n % counter == 0:
            sum = sum + counter
        counter += 1
 
    if sum == n:
        return True
    return False