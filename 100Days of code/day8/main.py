def greet():
    print("Bonjour")
    print("Good Morning")
    print("Buenos Dia")

greet()

#ex 1 random
import random , math


height = random.randint(1,11)
width  = random.randint(1,11)
print(width,height)
def cans(height, width):
         x = width
         y= height
         print(x,y)
         number_of_cans = (height*width)/5
         return math.ceil(number_of_cans)

print(cans(height=height,width=width))

#ex 1 input 
#Write your code below this line 👇
import math
def paint_calc(height, width,cover):
         number_of_cans = (height*width)/5
         print(f"You'll need {math.ceil(number_of_cans)} cans of paint.")



#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

