import random

#The difference between difficulty 0 codes and difficulty 1 codes are almost same. Only the lives and the gap between numbers will change.
#This game was built for educational purposes.


difficulty = int(input("Select Difficulty: (0 = Easy)(1 = Medium)(2 = Hard)(3 = Impossible)"))
print("Selected the difficulty. Bonne chance!")
if (difficulty == 0): #Easy
    computerSelection = random.randint(0,10) #Selects a random number between 0 and 10. This has been defined to a variable named "computerSelection"
    lives = 10 #Lives count
    point = 0 #Point count
    while True:
        playerSelection = int(input("Enter a number (0 = Exit): ")) #Waiting input from the player
        if (playerSelection == 0): #if player presses 0
            break #exits the code
        if(playerSelection == computerSelection): #If players selection is same as computer's random selection;
            print("Congrats, you find the number. You had",lives,"Lives") #You will win the game.
            point = point + lives #Adds points as high as your remaining lives. If you have 3 lives, you will get 3 points.
            print(lives,"Added to your point. Total point: ",point) #Outputs the result of addition of points.
        if(playerSelection <= computerSelection): #If player's selection is lower than computer's selection
            print("Guess a higher number, Remaining lives: ",lives-1) # You will lose 1 live and prints "lower the number".
            lives = lives - 1
            continue #This makes the game playable over and over again.
        else:
            print("Guess a lower number, Remaining lives: ",lives-1) #or "raise up the number".
            lives = lives -1
        if (lives == 0):
            print("You have lost all of your lives. The time will collapse now.")
            break #if your lives drops to 0, you will lose the game. Which ultimately leads to stopping the code.

if (difficulty == 1): #Medium
    computerSelection = random.randint(0,25)
    lives = 7
    point = 0
    while True:
        playerSelection = int(input("Enter a number (0 = Exit): "))
        if (playerSelection == 0):
            break
        if(playerSelection == computerSelection):
            print("Congrats, you find the number. You had",lives,"Lives")
            point = point + lives
            print(lives,"Added to your point. Total point: ",point)
        if(playerSelection <= computerSelection):
            print("Guess a higher number, Remaining lives: ",lives-1)
            lives = lives - 1
            continue
        else:
            print("Guess a lower number, Remaining lives: ",lives-1)
            lives = lives -1
        if (lives == 0):
            print("You have lost all of your lives. The time will collapse now.")
            break
if (difficulty == 2): #Hard
    computerSelection = random.randint(0,100)
    lives = 5
    point = 0
    while True:
        playerSelection = int(input("Enter a number (0 = Exit): "))
        if (playerSelection == 0):
            break
        if(playerSelection == computerSelection):
            print("Congrats, you find the number. You had",lives,"Lives") #
            point = point + lives
            print(lives,"Added to your point. Total point: ",point)
        if(playerSelection <= computerSelection):
            print("Guess a higher number, Remaining lives: ",lives-1)
            lives = lives - 1
            continue #This makes the game playable over and over again.
        else:
            print("Guess a lower number, Remaining lives: ",lives-1)
            lives = lives -1
        if (lives == 0):
            print("You have lost all of your lives. The time will collapse now.")
            break
if (difficulty == 3): #Impossible
    computerSelection = random.randint(0,1000)
    lives = 2
    point = 0
    while True:
        playerSelection = int(input("Enter a number (0 = Exit): "))
        if (playerSelection == 0):
            break #exits the code
        if(playerSelection == computerSelection):
            print("Congrats, you find the number. You had",lives,"Lives")
            point = point + lives
            print(lives,"Added to your point. Total point: ",point)
        if(playerSelection <= computerSelection):
            print("Guess a higher number, Remaining lives: ",lives-1)
            lives = lives - 1
            continue
        else:
            print("Guess a lower number, Remaining lives: ",lives-1)
            lives = lives -1
        if (lives == 0):
            print("You have lost all of your lives. The time will collapse now.")
            break