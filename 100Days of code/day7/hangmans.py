import random 

word_list = ["fashion","inconsistent","Malware"]

chosen_word = random.choice(word_list)
chosen_word = chosen_word.lower()

guess = input ("Guess a letter: \n:").lower()

for i in chosen_word:
    if i == guess:
        print("Right")
    else:
        print("Nah Bruhv")
    
for i in range(0,len(chosen_word)):   
    word_list.append("_")