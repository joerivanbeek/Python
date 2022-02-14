import random

computerwin = 0
userwin = 0

options = ["rock", "paper", "scissors"]

while True:
    user = input("Type Rock, Paper, Scissors or Quit: ").lower()
    if user == "quit":
        break #end program
    
    if user not in options: #returns if value is part of list
        continue #returns to start of loop
    
    number = random.randint(0,2)
    #0=R, 1=P, 2=S
    computer = options[number]
    print("Computer picked", computer)
    
    if user == "rock" and computer == "scissors":
        print("You won!")
        userwin += 1
        continue  
    elif user == "paper" and computer == "rock":
        print("You won!")
        userwin += 1
        continue 
    elif user == "scissors" and computer == "paper":
        print("You won!")
        userwin += 1
        continue
    else:
        print("You lost!")
        computerwin += 1
        continue
    
print("You won", userwin/computerwin ,"% of the games")

print("Press ENTER to quit the program")