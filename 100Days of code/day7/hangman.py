import random




print(" Hello and welcome to hangman")

#create worl list 
from hangman_words import word_list as wl

word_list = wl
life = 5
select_word = random.choice(word_list)  # select random word 
select_word = select_word.lower()      # lower case the letter  
hangman_list = []                       # empty list to hold the hangman 

import logo, stages

print(logo)

# for loop itterating over word to count empty spaces 
for i in range(0,len(select_word)):    # CREATE AN EMPTY LIST FOR LETTERS IB WORD "_"
    hangman_list.append("_")
print(select_word)
print(hangman_list)

end_of_game = False
guesses =[]
while not end_of_game:
    guess = input("Please enter a letter guess").lower() # user guess 
    if guess not in guesses:
        guesses+=guess
        for i in range(len(select_word)):     
            current_letter = select_word[i]
        # print(f"Current porsition: {i}\nCurrent letter: {current_letter}\nGuessed letter: {guess}")
            if guess == select_word[i]:
                hangman_list[i] = guess
        #     print("right")
        if guess not in select_word:
        # print("wrong")
            print(stages[life])
            life-=1
            #print(f"You have {life} lives left")
    else:
        print("Letter already used")
    print(hangman_list)

    if "_" not in hangman_list and life !=0 :
        end_of_game = True
        print("Congratulation")
    elif life ==0:
        end_of_game = True
        print("Failure")
        print(stages[0])