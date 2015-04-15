def string_matrix(matrix_width,string):
    new_string = ["|"]
    for str in string:
        for letter in str:
            new_string += letter + '|'
    return new_string

    
