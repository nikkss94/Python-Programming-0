def fib_number(n):
    list_number = [1,1]
    index = 0
    fib = 0
    
    if n == 1:
        return 1
    if n == 2:
        return 11
    if n >= 3:
        n -= 2
        while n > 0:
            list_number += [list_number[index] + list_number[index + 1]]
            index += 1
            n -= 1
    if len(list_number) >= 3:
        for number in list_number:
            fib = fib*10 + number
 
    return fib