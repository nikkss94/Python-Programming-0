def max_score(beers, fries):
    index = 0

    rating = 0

    beers = sorted(beers)
    fries = sorted(fries)

    for beer in beers:
        fry = fries[index]

        rating += beer * fry

        index += 1

    return rating

    

        

        
