import random
def move(player1, player2):
    if player1 == player2:
        return "Draw"
    elif (player1 =="Paper" and player2 =="Rock") or  (player1 =="Scissor" and player2 =="Paper")  or  (player1 =="Rock" and player2 =="Scissor"):
        return "You wins wins"
    else: 
        return "PC wins"
    
player_1=input("choose Paper or Rock or  Scissor: ")
random_move=["Paper","Rock","Scissor"]
player_2=random.choice(random_move)
print(f"your choice is {player_1} and the pc random choice is {player_2}")
result=move(player_1, player_2)
print (result)