import random

def play():
    user = input("Choose your character! 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])
  
    if user == computer: 
       return 'It\'s a tie!? Time for another round!'

    # r < p, p < s, s < r
    if is_win(user, computer):
        return 'You won!? Lucky shot, try again!'
    
    return 'You lost. As expected... Stand up and fight again!'

def is_win(player, opponent):
    # return True if player wins
    # r < p, p < s, s < r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())