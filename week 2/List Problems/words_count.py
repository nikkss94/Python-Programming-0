word = input("Enter word: ")
n = input("Enter n: ")
n = int(n)
 
counter = 0
words = []
 
while counter < n:
    l = input("")
    words += [l]
    counter += 1
 
start = 0
 
for wor in words:
    if wor == word:
        start += 1
 
print(word, " is found ",start," times ")
