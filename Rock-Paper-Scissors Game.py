
# REAL GAME WITH EXCITEMENT: 
import random
def RPS():
    print("Welcome to the Rock-Paper-Scissors game!\U0001F603 ")
    security_key = "aabbii"
    attempts = 3
    
    while attempts > 0:
        entered_key = input("Please enter the security key 🔑 to start the game: ")
        if entered_key == security_key:
            print("Security key accepted. You can now play the game!\U0001F602")
            break
        else:
            attempts -= 1
            print(f"Invalid key⚠️ . You have {attempts} attempts left.")
    
    if attempts == 0:
        print("You have used all attempts. Access denied❌ .")
        return
    

    while True:
        player_input = input("Enter your choice (rock, paper, scissors): ").lower()
        if player_input not in ["rock", "paper", "scissors"]:
            print("Invalid choice⚠️ . Please choose rock, paper, or scissors.")
            continue
        
        computer_choice = random.choice(["rock", "paper", "scissors"])
        
        print(f"You Choose {player_input} & the Computer Choose {computer_choice}.")
        
        if player_input == computer_choice:
            print("The game is a draw. 🤝")
        elif (player_input == "rock" and computer_choice == "scissors") or \
             (player_input == "paper" and computer_choice == "rock") or \
             (player_input == "scissors" and computer_choice == "paper"):
            print("You won the game! 🎉")
        else:
            print("You lost the game. 😢")
        
        play_again = input("Do you want to play again? (yes/no)\U0001F917: ").lower()
        if play_again != "yes":
            print("Hope You Enjoy The Game\U0001F618 \n Take Care & Stay Blessed\U0001F61A")
            break

RPS()






# import random
# win_matrix = [['D', 'W', 'L'], ['L', 'D', 'W'], ['W', 'L', 'D']]
# choice_list = ["Snake", "Water", "Gun"]
# dict_points = {'Snake': 0, 'Water': 1, 'Gun': 2}

# def play_game():
#     while True:
#         player_1 = input("Player1, select your option from (Snake, Water, Gun): ")
#         if player_1 not in dict_points:
#             print("Invalid choice. Please choose Snake, Water, or Gun.")
#             continue
        
#         player_2 = random.choice(choice_list)
#         print(f"System selected: {player_2}")

#         # Get the indices for the choices
#         player_1_index = dict_points[player_1]
#         player_2_index = dict_points[player_2]

#         # Determine the result
#         result = win_matrix[player_1_index][player_2_index]

#         # Print the result
#         if result == 'D':
#             print("The game is a draw.")
#         elif result == 'W':
#             print("Player 1 wins!")
#         else:
#             print("System wins!")

#         play_again = input("Do you want to play again? (yes/no): ").lower()
#         if play_again != "yes":
#             break

# play_game()
