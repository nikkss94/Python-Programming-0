def on_budget(books, budget):

    sum_books = sum(books)
    b = budget
    result = {"books_on_budget":0,
              "loan": 0,
             }
    books = sorted(books)
    for book in books:
        if b >= book:
            result["books_on_budget"] += 1
            b -= book
        if b <= 0:
            break
    if budget >= sum_books :
        return result
    elif budget  < sum_books:
        result["loan"] =  sum_books - budget
        return result



books = [10,12,0,15,30,13,0]
budget = 60
print(on_budget(books, budget))
