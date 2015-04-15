def magic_square(square):
    result = []
    for index in range(0, len(square)):
        element = square[index][index]
        result += [element]
        sum_result = sum(result)
    result_1 = []
    for i in range(3,0):
        element_1 = square[i][i]
        result_1 += [element_1]
        sum_r = sum(result_1)
    
        
           
            
            
    return result
    


square = [ [23, 28, 21], [22, 24, 26], [27, 20, 25] ]
print(magic_square(square))

                
        
        
        
