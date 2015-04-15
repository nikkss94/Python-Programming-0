from random import randint

n = input("Enter dice side: ")
n = int(n)
player_1 = input("Enter player1 name: ")
player_2 = input("Enter player2 name: ")

player1_roll = randint(1,n)
player2_roll = randint(1,n)
print(player_1 + " rolled: " + str(player1_roll))
print(player_2 + " rolled: " + str(player2_roll))

if player1_roll == player2_roll:
    print("Tie!")
elif player1_roll > player2_roll:
    print("The winner is: " + player_1)
else: 
    print("The winner is: " + player_2)

