print("Welcome to the Quiz")

question = "Do you want to play? "

playing = input(question)

if playing.lower() != "yes": #checks if not equal
    quit() #quit the script

#print(playing)

correct = 0

print("Okay let's play")

answer = input("What is 1 + 2? ")

if answer == "3":
    print("Good Job!")
    correct += 1 #adds 1 to count
else:
    print("Incorrect!")

answer = input("What is 2 + 4? ")

if answer == "6": #checks if equal
    print("Good Job!")
    correct += 1
else:
    print("Incorrect!")
    
answer = input("What is 1 - 1? ")

if answer == "0":
    print("Good Job!")
    correct += 1
else:
    print("Incorrect!")
    
answer = input("What is 1 * 2? ")

if answer == "2":
    print("Good Job!")
    correct += 1
else:
    print("Incorrect!")
    
answer = input("What is 10 / 2? ")

if answer == "5":
    print("Good Job!")
    correct += 1
else:
    print("Incorrect!")
    
score = ("You got "+str(correct)+" out of 5 questions correct!")
score1 = ("You got "+str((correct/5)*100)+"%")
         
print(score)
print(score1)
input('Press ENTER to exit') #makes script not auto close