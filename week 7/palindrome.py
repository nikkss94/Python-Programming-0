def is_string_palindrom(string):
    string = string.lower()
    new = ""
    new_string= ""
    f = False
    znaci = ["!"," ",",",".", "?"]

    for s in string:
        if s not in znaci:
            new += s
    for s_1 in new:
        new_string = s_1 + new_string

    if new_string == new:
        f = True
    return f
