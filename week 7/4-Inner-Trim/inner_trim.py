def inner_trim(string):
    new_string =  string.split()
    result_string = []
    result = ""
    for word in new_string:
        if len(new_string) == 1:
            return word
        if len(new_string) > 1:
            result += word + " "
    result = result[:-1]
    return result
    
        
