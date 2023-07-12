import random
Start = True
global answer
global Level
global guess
Level = 0
userInput = 0
global guesses_allowed
global guess_range
while Start == True:
    guesses_allowed = 3
    def play_again():
        global Start
        Decision = str(input('Do you want to play again?'))
        if Decision == 'yes':
            Start = True
            choose_level()
        else:
          quit()
    def reveal_answer():
        global guesses_allowed
        global guess
        global great
        for i in range(guesses_allowed):
            if (i == guesses_allowed - 1) and guess != answer:
                print("Sorry, you have run out of guesses. You lose!")
                print('The right answer is ' + str(answer))
                play_again()
            if guess == answer and guesses_allowed != 0:
                print('Right')
                play_again()
                break
            if guess < answer and guesses_allowed != 1:
                guesses_allowed = guesses_allowed - 1
                userInput = input('Try a higher number')
                guess = int(userInput)
                reveal_answer()
            if guess > answer and guesses_allowed != 1:
                guesses_allowed = guesses_allowed - 1
                userInput = input('Try a lower number')
                guess = int(userInput)
                reveal_answer()
    def choose_level():
        global guesses_allowed
        guesses_allowed = 3
        global Level
        global guess_range
        global answer
        global Start
        global guess
        Level = input('Which level do you want, Easy, Medium or Hard?')
        if Level == ('easy'):
            guess_range = 5
            # userInput = input("Guess a number between 1 and " + str(guess_range) + ": ")
        elif Level == ('medium'):
            guess_range = 10
            # userInput = input("Guess a number between 1 and " + str(guess_range) + ": ")
        elif Level == ('hard'):
            guess_range = 50
        else:
            print ('invalid word, please try again')
            choose_level()
        answer = int(random.randint(1, guess_range))
        userInput = input("Guess a number between 1 and " + str(guess_range) + ": ")
        guess = int(userInput)
        reveal_answer()
        '''
        Decision = str(input('Do you want to play again?'))
        if Decision == 'yes':
            Start = True
            choose_level()
        else:
            quit()'''
         #choose_level()
    choose_level()
    