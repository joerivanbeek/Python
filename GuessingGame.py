import random

start = 0
end = input("How high do you want to guess?" )#not included

if end.isdigit(): #returns true if it is an digit
    end = int(end)
    if end <= 0:
        print("Please input a number larger then 0!")
        quit()
else:
    print("Please input a number!")
    quit()

number = random.randrange(start, end)

#print (number)
tries = 0

while True:
    tries += 1
    guess = input("Guess a number: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Please input a number!")
        continue #repeats loop from start
    
    if guess == number:
        print("Good Job! It took you", tries, "tries to get the answer!")
        break
    elif guess > number: #second if statement
        print("Guess Again, you were above the number")
    else:
        print("Guess Again, you were below the number")

input('Press ENTER to exit')

