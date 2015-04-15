from random import randint
 
def generate_random_list(n, start, end):
    result = []
    counter = 0
    while counter < n:
        next_number = randint(start, end)
        result = result + [next_number]
 
        counter += 1
        
    return result