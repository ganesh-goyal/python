from random import randint,choice


print("lets play 'rock' 'paper' 'scissor' game -->")
player = input("enter the choice (rock,paper,scissor):")
print(player,'vs', end=' ')

cmp = randint(1,4)
print(cmp)

if cmp == 1:
  computer = 'rock'
elif cmp == 2:
  computer = 'paper'
else:
  computer = 'scissor'
  
print(computer)

if computer == player:
  print("match tie..! this match")
elif computer == 'rock' and player == 'paper':
  print("computer won..!")
elif player == 'rock'and computer == 'paper':
  print("player won..!")
elif player =='paper' and computer == 'scissor':
  print("computer won ....!!..yeah.. ")
elif player == 'scissor' and computer =='paper':
  print("player won this math...!1")
