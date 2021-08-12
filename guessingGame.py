import random
correctNo = random.randint(1,9)
print('Number Guessing Game')
name = input('What is your name?? ')
chances = 0
trials = 5

while chances < 5: 
    chances += 1
    guess = int(input('Guess a number(between 1 and 9) : '))
    if(guess > correctNo) : 
        trials = 5-chances
        print('Guess was too high!! : Guess a number lesser than' , guess , ' ; Chances left :' , trials)

    elif(guess < correctNo) : 
        trials = 5-chances
        print('Guess was too low!! : Guess a number greater than' ,  guess , ' ; Chances left :' , trials )

    else : 
         print('Congratulations !! You have won this game')
         print(name)
         break

if not chances < 5 :
    print("You Lose!! The number is" , correctNo)