def get_people_count(activity):
    counter = 0
 
    result = []
 
    for name in activity:
        if name not in result:
            result += [name]
            counter += 1
 
    print("All people on the concert are " + str(counter))
    return result
