def string_matrix(string):
    new_string = "|"
    for str in string:
        for letter in str:
            new_string += letter + '|'
            return new_string

    
