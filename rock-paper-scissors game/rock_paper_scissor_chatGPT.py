import random

def move(player1, player2):
    if player1 == player2:
        return "Draw"
    elif (player1 == "Paper" and player2 == "Rock") or  (player1 == "Scissor" and player2 == "Paper") or  (player1 == "Rock" and player2 == "Scissor"):
        return "You win!"
    else: 
        return "PC wins"

def get_user_choice():
    while True:
        choice = input("Choose Paper, Rock, or Scissor: ").capitalize()
        if choice in ["Paper", "Rock", "Scissor"]:
            return choice
        else:
            print("Invalid choice. Please choose Paper, Rock, or Scissor.")

def play_round():
    player_1 = get_user_choice()
    player_2 = random.choice(["Paper", "Rock", "Scissor"])
    print(f"Your choice is {player_1} and the PC's random choice is {player_2}")
    result = move(player_1, player_2)
    print(result)
    return result

def main():
    player_score = 0
    pc_score = 0
    rounds = 0

    while True:
        result = play_round()

        if "win" in result:
            player_score += 1
        elif "PC wins" in result:
            pc_score += 1

        rounds += 1
        print(f"Score: You {player_score} - PC {pc_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print(f"Thanks for playing! You played {rounds} rounds.")
            break

if __name__ == "__main__":
    main()
