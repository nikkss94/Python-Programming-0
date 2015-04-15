def sublist(list1, list2):
    f = False
    for l in list1:
        for l_1 in list2:
            if l == l_1:
                f = True
                break
    return f

list1 = ["Python"]
list2 = ["Python", "C++","C"]
