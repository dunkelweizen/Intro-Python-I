import random

def play_game():
    moves = ['rock', 'paper', 'scissors']
    winner_dict = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}

    player1_score = 0
    ai_score = 0
    print("Let's play a game! Choose rock, paper, scissors. Or you can quit by typing 'quit'!")
    player1_move = input()
    while player1_move != 'quit':
        ai_move = random.choice(moves)
        if player1_move not in moves:
            print("That's not a valid move. Choose rock, paper, scissors. Or you can quit by typing 'quit'!")
        elif player1_move == ai_move:
            print(f"You choose {player1_move}, Computer chose {ai_move}.")
            print("It's a draw!")
        elif winner_dict[ai_move] == player1_move:
            print(f"You choose {player1_move}, Computer chose {ai_move}.")
            print("Computer wins this round!")
            ai_score += 1
            print("Play again? Choose rock, paper, scissors. Or you can quit by typing 'quit'!")
        else:
            print(f"You choose {player1_move}, Computer chose {ai_move}.")
            print("You win this round!")
            player1_score += 1
            print("Play again? Choose rock, paper, scissors. Or you can quit by typing 'quit'!")
        print(f"Current score \nPlayer Score: {player1_score}\nComputer Score: {ai_score}")
        player1_move = input()


if __name__ == "__main__":
    play_game()
