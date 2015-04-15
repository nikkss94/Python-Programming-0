def to_digit(number):
    biggest = 0
    smallest = 0
    list_number = []
    list_numbers = []
    while number != 0:
        a = number % 10
        list_numbers += [a]
        number = number // 10
    list_numbers = sorted(list_numbers)
 
    for c in list_numbers:
        list_number = [c] + list_number
 
    for b in list_number:
        biggest = biggest * 10 + b
    for d in list_numbers:
        smallest = smallest*10 + d
 
    
    print("The biggest is: ",biggest)
    print("The smallest is: ",smallest)