# Just wanted you to know that I didn't ignore Sam's suggestion to covert back
# and forth from string to list to string.  But, when doing my research, I first 
# came accross the slicing/concatenation method for replacing, so I stuck with
# strings throughout, which seemed simpler for me (and worked).

import random

word_list = ['HAWK', 'FALCON','PIGEON', 'JUNCO', 'PELICAN', 'SWIFT', 'TUCAN', 'CRANE', 'HERON']

secret = random.choice(word_list)
print(secret)

secret_output = ''

for n in secret:
    secret_output = secret_output + "_"
print(f"This is the number of letters in the word: ")
print(secret_output)


correct_count = 0
incorrect_count = 0
t = True
while t:
    guess = input("\nPlease, guess a letter:  ")

    if guess.upper() in secret:
        print(f"\n{guess.title()} goes here:")
        correct_count = correct_count + 1
        # printing count for testing
        # end count test

        i = secret.index(guess.upper())
        
        secret_output = secret_output[:i] + guess.upper() + secret_output[i+1:]
        print(secret_output)
        if correct_count == len(secret):
            print(f"Congratulations! You've won!")
            t=False
        else:
            continue


    else:
        print(f"\nSorry, {guess.title()} isn't in this word!")
        incorrect_count = incorrect_count + 1
        if incorrect_count < 7:
            continue
        else:
            print(f"\nUnfortutnately you have have exceeded the allowed 7 incorrect guesses.") 
            print(f"\nThis was the word you were trying to guess: ")
            print(f"\t{secret}.") 
            break      



