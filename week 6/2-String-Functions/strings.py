def str_reverse(n):
    new_list = []
    for a in n:
        new_list = [a] + new_list
    return new_list
    
def join(delimiter, items):
    result = ""
    last_index = len(items) - 1
 
    for index in range(0, last_index):
        item = items[index]
        result = result + item + delimiter
 
    result += items[last_index]
 
    return result
    
def startswith(search,string):
    for index in range(0,len(search)):
        if search[index] == string[index]:
            return True
        else:
            return False
            
def endswith(search,string):
    new_string = []
    new_search = []
    for s in string:
        new_string = [s] + new_string
    for a in search:
        new_search = [a] + new_search
    for index in range(0,len(search)):
        if new_search[index] == new_string[index]:
            return True
        else:
            return False
 
def white_spaces_count(string):
    count_white_spaces = 0
 
    for ch in string:
        if ch != " ":
            break
 
        count_white_spaces += 1
 
    return count_white_spaces
 
def trim(string):
    result = ""
 
    start = white_spaces_count(string)
    end = len(string) - white_spaces_count(str_reverse(string))
 
    for i in range(start, end):
        result += string[i]
    return result
