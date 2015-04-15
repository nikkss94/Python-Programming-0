def square(n):
    return n ** 2
 
 
def fact(n):
 
    counter = 1
    sum = 1
 
    while counter <= n:
        sum = sum*counter
        counter += 1
    return sum
    
 
def count_elements(items):
    count = 0
    for n in items:
        count += 1
    return count
 
 
def member(x,xs):
    f = False
    for s in xs:
        if x == s:
            f = True
            break
    return f
 
 
def square(n):
    return n ** 2
 
 
def fact(n):
 
    counter = 1
    sum = 1
 
    while counter <= n:
        sum = sum*counter
        counter += 1
    return sum
    
 
def count_elements(items):
    count = 0
    for n in items:
        count += 1
    return count
 
 
def member(x,xs):
    f = False
    for s in xs:
        if x == s:
            f = True
            break
    return f
 
 
def grades_that_pass(students,grades,limit):
 
    result = []
    i = 0
 
    for grade in grades:
        student = students[i]
        if grade >= limit:
            result = result + [student]
        i += 1
    return result 