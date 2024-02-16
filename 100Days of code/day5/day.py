#ex 1 average height using for loops
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
number_of_student = 0
total_student_height = 0
for i in student_heights:
    number_of_student += 1
    total_student_height+=i

avr_height = total_student_height/number_of_student

print(round(avr_height))


#ex 2 
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
high_score = max(student_scores)
print(f"The highest score in the class is: {high_score}")
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
high_score = 0 
for i in student_scores:
    if i> high_score:
        high_score = i

print(f"The highest score in the class is: {high_score}")



#ex 3 calculate all even number from 1 to 100 
#Write your code below this row 👇
total =0
for i in range(1,101):
    if i %2 ==0:
        total+=i
print(total)
# diffrent solving method
#for i in range(1,101,2):
#total+=i
#print(total)
#
#

# ex 4  
#Write your code below this row 👇

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0: #and i % 3 != 0:
        print("Buzz") 
    elif i % 3 == 0:# and i % 5 != 0:
        print("Fizz") 
    else:
        print(i)

# diff