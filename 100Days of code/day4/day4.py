import random
#ex 1

head_or_tails = random.randint(0,1)
if head_or_tails == 0:
    print("Heads")
else:
    print("Tails")

#ex 2
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
names_len = len(names)
x = random.randint(0,names_len-1)
# x= random.coice(names) quicker method
print(names[x]+ " is going to but the meal today.")

#ex 3
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
col = int(position[0])-1
row = int(position[1])-1 
map[row][col] = 'X'
print(map)