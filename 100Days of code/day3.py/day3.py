#ex 1 odd or even numbers 

number = int(input("Which number do you want to check? "))

if number % 2 == 0 or number % 2 == 2:
    print("This is an even number.")
else:
    print("this is an odd number.")



#ex 2 BMI Calculator

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))


BMI = round(weight/(height**2))
if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI <=0:    
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI <35:
    print(f"Your BMI is {BMI}, you are obese.")
else:
    print(f"Your BMI is {BMI}, you are clinicaly obese.")


#ex 3 leap  year 

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 != 0 or year % 400 ==0:
        print("Leap year.")
else:
    print("Not leap year.")

# ex 4 pizza order 
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
total =0
if   size == "L":
    total+= 25
elif size == "M":
    total+= 20
elif size == "S":
    total+= 15
else:
    print("Please select a size")
if add_pepperoni == "Y":
    if size == "L" or size =="M":
        total+= 3
    else:
        total+= 2
if extra_cheese =="Y":
    total+= 1
print(f"Your final bill is: ${total}")


#ex 5 love calculaor ??  Check how many time letter shows up in both words true count 1  and love 
# name1 = input("What is your name? \n")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_string = name1 +name2
combined_string_lower = combined_string.lower()

t = combined_string_lower.count("t")
r = combined_string_lower.count("r")
U = combined_string_lower.count("u")
e =  combined_string_lower.count("e") 

l = combined_string_lower.count("l")
o = combined_string_lower.count("o")
v = combined_string_lower.count("v")
e = combined_string_lower.count("e")


true_count = t+r+u+e
love_count = l+o+v+e

love_score = str(true_count)+str(love_count)
love_score_int = int(love_score)
if love_score_int <10 or love_score_int>90:
    print(f"Your score is {love_score_int}, you go together like coke and mentos.")
elif love_score_int <50 and love_score_int>40:
    print(f"Your score is {love_score_int}, you are alright together.")
else:
    print(f"Your score is {love_score_int}.")


















# ex 5 my method 
count1= 0 
count2 = 0
name1 = name1.lower()
name2 = name2.lower()
x = "true"
y = "love"
for i in name1:
    if i in x:
         count1+=1
    if i in y:
         count2 +=1
for i in name2:
    if i in x:
         count1+=1
    if i in y:
         count2 +=1
total= str(count1)+str(count2)
total_int = int(total)
if total_int <10 or total_int>90:
    print(f"Your score is {total_int}, you go together like coke and mentos.")
elif total_int <50 and total_int>40:
    print(f"Your score is {total_int}, you are alright together.")
else:
    print(f"Your score is {total_int}.")
