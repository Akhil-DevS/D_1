rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
game=[rock,paper,scissors]
while(True):
  enter_choice=input('enter you choice(rock/paper/scissors)').lower()
  x=random.randint(0,2)
  y= 10
  if(enter_choice=='rock'):
    print(f'computer choice\n{game[x]}')
    print(f'your value\n{game[0]}')
    y=0
  elif(enter_choice=='paper'):
    print(f'computer choice\n{game[x]}')
    print(f'your choice\n{game[1]}')
    y=1
  elif(enter_choice=='scissors'):
    print(f'computer choice\n{game[x]}')
    print(f'your choice\n{game[2]}')
    y=2
  else:
    print('wrong input.....!!!!')
  if(x==0 and y==1):
    print('you win this round')
  elif(x==1 and y==2):
    print('you win this round')
  elif(x==2 and y==0):
    print('you win this round')
  elif(x==y):
    print('its a draw')
  else:
    print('you lose this round')
  cont=input('wanna play again?(y/n)').lower()
  if(cont=='n'):
    break