from random import randint
n = input("Enter sides: ")
n = int(n)
k = randint(1,n)
p = randint(1,n)
print ("First roll:\n",k)
print ("Second roll:\n",p)
sum_of_all = k + p
print("Sum is:\n", sum_of_all)


