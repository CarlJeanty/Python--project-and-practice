print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

Forest_mountain = input("Aye me Captain Which direction should we go. Through the 'forest' or climb the 'mountain'.")
FM_lower=Forest_mountain.lower()
if FM_lower == "forest":
    run_or_jump= input("Captain Georgy boy step on a rope a bolders coming down do we 'run' or 'climb'.")
    rj_lower= run_or_jump.lower()
    if rj_lower == "run":
        print("Game Over:\n You have been capture by the natives numerous traps and have become soup")
    elif:
        print("Game Over:\n you climb to find natives with spears and snakes are waiting above you fight your way out but the crew is dead and you are sick will you make it home alive")
    else:
        print("Game Over:\n The crew confused with silence of their captain hesitated and squash!!! bolder wins FATALITY 'human soup' we eat  ")
elif FM_lower == "mountain":
    hide_or_fight =input("Captain birds on thee way i see a cavern do we 'hide' or do we 'fight'?")
    hf_lower=hide_or_fight.lower()
    if hf_lower == 'hide':
        print("Game Over: You have entered the beast lair it glares as it awakes the bease is suprise.\n Never has the beast witness a meal offering itself and it will glady feast")
    elif hf_lower == 'fight':
        print("the conflict is won, Climbing to the top you find golden rubies, pearls diamonds and the Crew is excited having becoming rich.\n : CONGRATULATION ")\
    else:
        print("Game Over:\n Withought an answer the crew undertstands panics and throws you to the birds to save themselves and run back to the ship")
else: 
    print("The crew fails to understand and force mutiny to go back home.")