def hash_them(keys,values):
    people = {}
    index = 0

    for key in keys:
        if index <len(values):
            people[key] = values[index]
        else:
            people[key] = None
        index += 1

    return people


        
        
    
