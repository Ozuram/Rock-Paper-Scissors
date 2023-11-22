import random



def play():
  playagain = True
  score = 0
  while playagain: 

      user_input = input("Choose your character! 'r' for rock, 'p' for paper, 's' for scissors\n")
      computer = random.choice(['r', 'p', 's'])

      if user_input == computer: 
         print( 'It\'s a tie!? Time for another round!')

      # r < p, p < s, s < r
      elif is_win(user_input, computer):
        print('You won!? Lucky shot, try again!')
        score += 1

      else:   
          print('You lost. As expected... Stand up and fight again!')


      playagain = input("Play again? (y/n)\n") 
      if playagain == 'n':
         print('Thanks for playing!')
         break
  print(f'You won number of times: {score}')

def is_win(player, opponent):
    # return True if player wins
    # r < p, p < s, s < r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())

input_list = ["rock", "paper", "scissors"]

print(input_list[1])
