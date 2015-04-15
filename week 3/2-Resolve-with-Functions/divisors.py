def divisors(n):
    counter = 1
    divisors_list = []
    while counter < n:
        if n % counter == 0:
            divisors_list += [counter]
        counter += 1
    return divisors_list