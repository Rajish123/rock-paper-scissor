import random

game_list = ['rock', 'paper', 'scissor']
comp_point = 0
player_point = 0

while True:
    print("Welcome to rock paper scissor ")
    print("press (1) for rock\n press (2) for paper\n press (3) for scissor\n\n")
    computer = random.choice(game_list)
    try:
        player = int(input("Enter your choice: "))
    except ValueError:
        print("Please use number")
        break
    if computer == "rock":
        if player == 1:
            print(f"computer choosed {computer} and you choosed {game_list[0]} ")
            print("Tie game!!")

        elif player == 2:
            print(f"computer choosed {computer} and you choosed {game_list[1]} ")
            print("You win!!")
            player_point += 1
        else:
            print(f"computer choosed {computer} and you choosed {game_list[1]} ")
            print("You lose!!")
            comp_point += 1
        
    elif computer == "paper":
        if player == 1:
            print(f"computer choosed {computer} and you choosed {game_list[0]} ")
            print("You lose!!")
            comp_point += 1

        elif player == 2:
            print(f"computer choosed {computer} and you choosed {game_list[1]} ")
            print("Tie game!!")
        else:
            print(f"computer choosed {computer} and you choosed {game_list[2]} ")
            print("You win!!")
            player_point += 1
        
    elif computer == "scissor":
        if player == 1:
            print(f"computer choosed {computer} and you choosed {game_list[0]} ")
            print("You win!!")
            player_point += 1

        elif player == 2:
            print(f"computer choosed {computer} and you choosed {game_list[1]} ")
            print("You lose!!")
            comp_point += 1
        else:
            print(f"computer choosed {computer} and you choosed {game_list[2]} ")
            print("Tie game!!")

    print(f"Score is:\n Computer = {comp_point} \n Player = {player_point} ")
        
    decision = input("Play again?(y/n): ").lower()
    if decision == "y":
        continue
    else:
        print(f"Total point scored\n Computer = {comp_point} \n Player = {player_point} ")
        break





    
    
