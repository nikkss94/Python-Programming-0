def string_matrix(matrix_width,strings):
    new_string = "|"
    new_strings = []
    result = []
    for string in strings:
        x = matrix_width - len(string)
        if x >= 0:
            for s in string:
                new_string +=  s + "|"
            while x > 0:
                new_string += "X|"
                x -= 1
        if x < 0:
            string = string[:x]
            for word in string:
                new_string +=  word + "|"
                
        new_strings += [new_string]
        new_string = "|"
    l = matrix_width - len(new_strings)
    count = l
    k = "|" + "X|" * matrix_width
    while count > 0:
        new_strings += [k]
        count -= 1
    if l < 0:
        new_strings = new_strings[:l]              
            
    return new_strings
                
        

