# These are instructions to GitHub Copilot

# Write code for the popular rock, paper and scissors game. 
# The game should be played between two players. 
# The game should be played in rounds, where each player selects one of the three options. 

import random

def rock_paper_scissors():
    choices = ['rock', 'paper', 'scissors']
    player1 = input('Player 1, enter your choice: ').lower()
    player2 = random.choice(choices)
    print(f'Player 2 chose: {player2}')
    
    if player1 not in choices:
        print('Invalid choice. Please enter rock, paper or scissors.')
        return
    
    if player1 == player2:
        print('It\'s a tie!')
    elif (player1 == 'rock' and player2 == 'scissors') or \
         (player1 == 'paper' and player2 == 'rock') or \
         (player1 == 'scissors' and player2 == 'paper'):
        print('Player 1 wins!')
    else:
        print('Player 2 wins!')

def main():
    while True:
        rock_paper_scissors()
        play_again = input('Do you want to play again? (yes/no): ').lower()
        if play_again != 'yes':
            print('Thanks for playing!')
            break

if __name__ == "__main__":
    main()