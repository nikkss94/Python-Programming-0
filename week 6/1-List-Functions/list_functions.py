def head(list_function):
    return list_function[0]
    
def last(list_function):
    return list_function[len(list_function)-1]
    
def tail(list_function):
    new_list = []
    for index in range(1,len(list_function)):
         new_list += [list_function[index]]
    return new_list
    
def equal_lists(list_function1,list_function2):
    
    for index in range(0,len(list_function1)):
        if list_function1[index] == list_function2[index] and len(list_function1) == len(list_function2):
            return True
 
        else:
            return False
 
def count_item(search, items):
    count = 0
 
    for item in items:
        if item == search:
            count += 1
 
    return count
    
def take(n, items):
    result = []
 
    for index in range(0, min(n, len(items))):
        result += [items[index]]
 
    return result
    
def drop(n, items):
    result = []
 
    for index in range(n, len(items)):
        result += [items[index]]
 
    return result
    
def reverse(items):
    result = []
 
    last_index = len(items) - 1
 
    while last_index >= 0:
        result += [items[last_index]]
        last_index -= 1
 
    return result
