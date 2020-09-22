# -------------------------------------------------
# LAB 3 - Word Jumble Game
# -------------------------------------------------

import random

print('_' * 60)
print('                WELCOME TO WORD JUMBLE GAME       ')
print('_' * 60)


# Create a word list
words = ['golden', 'yellow', 'orange', 'maroon', 'magenta']
random.shuffle(words)

# Pick a word

points = 0

for word in words:
    
    # Jumble the word
    temp = list(word)
    random.shuffle(temp)
    jword = ' '.join(temp)
    
    # Present it to the user
    print('Guess this: ', jword)
    
    # Ask for the user's guess
    uword = input('? ')
    
    # Compare and give result
    if(uword == word):
        points += 1

    # Repeat the process for rest of the words

# Give the final score

print('_' * 60)

if(points == 5):
    print('\nExcellent playing!')
elif(2 < points < 5):
    print("\nGood!")
else:
    print("\nImprovement needed")

print('THANK YOU')
