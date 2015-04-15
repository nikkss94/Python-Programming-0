words = input("")
 
count = 0
f = False
a_words = "aeiouyAEIOUY"
 
for word in words:
    if word in a_words:
        count += 1
print(words, " - ",count)