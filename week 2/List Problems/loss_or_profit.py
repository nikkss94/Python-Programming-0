def loss_or_profit(income,outcome):

    sum_income = 0
    sum_outcome = 0

    for a in income:
        sum_income += a
    for b in outcome:
        sum_outcome += b
    if sum_income - sum_outcome > 0:
        return "+" + str(sum_income - sum_outcome)
    elif sum_income - sum_outcome < 0:
        return str(sum_income - sum_outcome)
    elif sum_income == sum_outcome:
        return "=0"
    
        
