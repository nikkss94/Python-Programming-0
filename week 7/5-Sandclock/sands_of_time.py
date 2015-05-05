def sands_of_time(odd_number):
    count = odd_number
    x = 1
    while count > 0:
        print("."*x + "*"*count + "."*x)
        count -= 2
        x += 1
    count = 3
    x -= 2
    while count <= odd_number:
        print("."*x + "*"*count + "."*x)
        count += 2
        x -= 1
