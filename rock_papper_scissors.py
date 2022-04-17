import random
import os
from time import sleep
from typing import List

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def randomItem():
    List=[1, 2, 3]
    pc=random.choice(List)
    return pc
    
clearConsole()
print("WELCOME ON ROCK-PAPPER-SCISSORS\n")    
sleep(3)
clearConsole()
flag=1
print("HOW MANY GAMES DO YOU WANT THE MATCH TO HAS?")
games=input()
g=int(games)
player=0
computer=0
sleep(1)

for i in range(0, g):
   clearConsole()
   sleep(2)
   print("1-->Rock\n2-->Papper\n3-->Scissors")
   print("Choose your item: ")
   sth=input()
   item=int(sth)
   p=randomItem()
   pc=int(p)
   if (item==1):
       if (pc==1):
        print("TIE!!!")
        print("Computer:Rock")
       elif(pc==2):
         print("COMPUTER WINS!!!")
         print("Computer:Papper")
         computer+=1
       elif(pc==3):
         print("PLAYER WINS")
         print("Computer:Scissors")
         player+=1
   elif (item==2):
       if (pc==1):
        print("PLAYER WINS!!!")
        print("Computer:Rock")
        player+=1
       elif(pc==2):
         print("TIE!!!")
         print("Computer:Papper")
       elif(pc==3):
         print("COMPUTER WINS")
         print("Computer:Scissors")
         computer+=1
   elif (item==3):
       if (pc==1):
        print("COMPUTER WINS!!!")
        print("Computer:Rock")
        computer+=1
       elif(pc==2):
         print("PLAYER WINS!!!")
         print("Computer:Papper")
         player+=1
       elif(pc==3):
         print("TIE!!!")
         print("Computer:Scissors")
   sleep(1.5)

if player>computer:
    print("Player wins the match!")
    print("Player:",player,"Computer:",computer) 
elif computer>player:
    print("Computer wins the match!")
    print("Player:",player,"Computer:",computer)
else :
    print("The match is a total Tie!")
    print("Player:",player,"Computer:",computer)