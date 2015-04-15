def calculate_coins(sum):
    result = {}
    coins = [100,50,20,10,5,2,1]

    sum = round(sum * 100)

    for coin in coins:
        money = sum // coin
        result[coin] = money
        sum = sum  - money * coin

    return result
