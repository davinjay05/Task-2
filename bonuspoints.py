word_to_guess= 'cat'

while True:

    guess1 = input('Guess the First letter: ')
    if guess1 != 'c':
        print('Try again')
    else :
        print("CONGRATS YOU GUESSED THE FIRST WORD")
        break

while True:
    guess2 = input('Guess the Second letter: ')
    if guess2 != 'a':
        print('Try again')
    else :
        print('CORRECT! TWO DOWN!, ONE GUESS TO GO!')
        break
while True :
    guess3 = input('Guess the Last letter: ')
    if guess3 != 't':
        print('Try again')
    else :
        print('CONGRATULATIONS! YOU HAVE GUESSED ALL LETTERS GREAT JOB!')
        print('Thank You For Playing!')
        break
def save (character):
    with open('guess.txt', 'w') as file:
        file.write(character)
    print('Your File has been saved')
user_confirmation =input('Do you Want to save the game ? Yes/No')
if user_confirmation == 'Yes':
    save('cat')
else :
    print('Thank You For Playing!')


    

