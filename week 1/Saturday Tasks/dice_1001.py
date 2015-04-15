from random import randint

player_one = input("Enter first player: ")
player_two = input("Enter second player: ")

first_player = 1001
second_player = 1001

while True:
    
    sum = 0
    counter = 1
    while counter <= 6:
        n = randint(1,6)
        sum = sum + n
        counter += 1
  
        break
    if  first_player > 0:
        first_player -= sum
    elif first_player < 0:
        first_player += sum

    print(player_one + " rolls: " + str(sum) + " and has a score of: " + str(first_player))

    if first_player == 0:
        print(player_one, " wins ")
        break

    
    sum = 0
    counter = 1
    while counter <= 6:
        n = randint(1,6)
        sum = sum + n
        counter += 1
   
        
    if  second_player > 0:
        second_player -= sum
    elif second_player < 0:
        second_player += sum

    print(player_two + " rolls: " + str(sum) + " and has a score of: " + str(second_player))

    if second_player == 0:
        print(player_two, " wins ")
        break
        
            
        
    
