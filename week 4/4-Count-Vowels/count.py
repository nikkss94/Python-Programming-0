def count_vowels_consonants(word):

    result = {"vowels": 0,
              "consonants": 0,
             }

    vowels = "aeiouyAEIOUY"
    consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"


    for a in word:
        if a in vowels:
            result["vowels"] += 1

        elif a in consonants:
            result["consonants"] += 1

    return result
            
        
            
