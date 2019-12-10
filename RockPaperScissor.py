from random import random


user_input = input('Choose Rock, Paper or Scissor: ')
computer_input = int(random()*10)

dict = {'Rock': 3, 'Paper': 5, 'Scissor' :7}

if(computer_input < 4):
    computer_input = 3
elif(computer_input >3 and computer_input < 7):
    computer_input= 5
else:
    computer_input= 7

if(computer_input == dict[user_input]):
    print('It is a tie.')
elif(computer_input < dict[user_input]):
    print('You win.')
else:
    print('Computer wins.')