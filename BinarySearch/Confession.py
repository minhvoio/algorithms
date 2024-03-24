import time
import os
from pyfiglet import Figlet

os.system('clear')
print('Welcome to the Three Numbers Game! \n')

choose = 0

menu = {
  1: """There's ONE thing you've already known.""",
  2: """There're TWO ways to answer.""",
  3: """There're THREE words in this sentence."""
}

numbers = [1, 2, 3]

while numbers:  
  choose = int(input(f'Pick a number from {numbers}: '))

  match choose:
    case 1:
      print(menu.get(1), "\n")      
    case 2:
      print(menu.get(2), "\n") 
    case 3:
      print(menu.get(3), "\n") 
  
  if choose in numbers:
    numbers.remove(choose)
    time.sleep(1)

f = Figlet(font='slant')

print('Can you guess what is it?\n')

for i in range(5, 0, -1):
  time.sleep(1)
  print(i)  

print('\n----------------------------------------\n')

message = "I LIKE YOU"
lines = message.split()

for line in lines:
    print(f.renderText(line))
    time.sleep(5 / len(lines))  

print('\n----------------------------------------\n')
    