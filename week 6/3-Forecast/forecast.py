def forecast(days):
    sun = snow = rain = 0
 
    for day in days:
        if "snow" == day:
            snow += 1
        elif "rain" == day:
            rain += 1
        elif "sunshine" == day:
            sun += 1
    if rain > sun or rain > snow:
        return "rain"
    if sun > rain or sun > snow:
        return "sun"
    if snow > sun or snow > rain:
        return "snow"
    if sun == snow and sun > rain:
        return "rain"
    if sun == rain and sun > snow:
        return "snow"
    if rain == snow and rain > sun:
        return "sun"
    if rain == snow == rain:
        return days[len(days)]
