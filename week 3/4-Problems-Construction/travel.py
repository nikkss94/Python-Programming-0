def travel(travels):
    total_sum = 0
 
    for travel in travels:
        if travel >= 23:
            total_sum += 23
        else:
            total_sum += travel * 1
 
        if total_sum >= 50:
            return 50
 
    return total_sum