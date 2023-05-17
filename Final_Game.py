import random
import os

# Set up the scoreboard
scoreboard = {'Player 1': 0, 'Player 2': 0, 'Computer': 0}

# Define the game function
def game():
    print('Welcome to Rock Paper Scissors!')
    while True:
        # Ask the player(s) to choose rock, paper, or scissors
        if num_players == 1:
            while True:
                player_choice = input('Enter your choice (rock/paper/scissors): ')
                if player_choice.lower() not in ['rock', 'paper', 'scissors']:
                    print('Invalid input!')
                else:
                    break
        else:
            while True:
                player_choice = input('Player 1: Enter your choice (rock/paper/scissors): ')
                if player_choice.lower() not in ['rock', 'paper', 'scissors']:
                    print('Invalid input!')
                else:
                    os.system('cls')
                    break
                    
            while True:
                player2_choice = input('Player 2: Enter your choice (rock/paper/scissors): ')
                if player2_choice.lower() not in ['rock', 'paper', 'scissors']:
                    print('Invalid input!')
                else:
                    os.system('cls')
                    break
                    
        
        # Generate a random choice for the computer if playing against it
        if num_players == 1:
            computer_choice = random.choice(['rock', 'paper', 'scissors'])
        
        # Determine the winner
        if num_players == 1:
            print(f'Computer chooses {computer_choice}!')
            if player_choice == computer_choice:
                print('Tie!')
            elif (player_choice == 'rock' and computer_choice == 'scissors') or (player_choice == 'paper' and computer_choice == 'rock') or (player_choice == 'scissors' and computer_choice == 'paper'):
                print('You win!')
                scoreboard['Player 1'] += 1
            else:
                print('Computer wins!')
                scoreboard['Computer'] += 1
        else:
            print(f'Player 1 chooses {player_choice}!')
            print(f'Player 2 chooses {player2_choice}!')
            if player_choice == player2_choice:
                print('Tie!')
            elif (player_choice == 'rock' and player2_choice == 'scissors') or (player_choice == 'paper' and player2_choice == 'rock') or (player_choice == 'scissors' and player2_choice == 'paper'):
                print('Player 1 wins!')
                scoreboard['Player 1'] += 1
            else:
                print('Player 2 wins!')
                scoreboard['Player 2'] += 1
        
        # Print the updated scoreboard
        print('Scoreboard:')
        for player, score in scoreboard.items():
            print(f'{player}: {score}')
        
        # Ask the player(s) if they want to play again
        while True:
            play_again = input('Do you want to play again? (y/n): ')
            if play_again.lower() in ['y', 'n']:
                break
            else:
                print('Invalid input!')
        if play_again.lower() != 'y':
            break

# Ask the player how many people are playing
while True:
    num_players = input('Are you playing alone or with another person? (1/2): ')
    if num_players in ['1', '2']:
        num_players = int(num_players)
        os.system('cls')
        break
    else:
        print('Invalid input!')

# Start the game
game()
