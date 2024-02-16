#ex1 add the two digit string
two_digit_number = input("type a two digit number: \n")
first_d = two_digit_number[0]
second_d= two_digit_number[1]
result = int(first_d)+int(second_d)
print(int(two_digit_number[0])+int(two_digit_number[1]))



#ex2
weight = (input('Please enter your weight in Kg: \n'))
height = (input('Please enter your height in m: \n'))
weight = float(weight)
height = float(height)
BMI    = round(weight/(height**2))
print(BMI)
print("your BMI is "+str(BMI))


#ex3
age     = input("What is your age ")
age_int = int(age)

years_from_90 = 90-age_int
days   = 365 * years_from_90
weeks  = 52  * years_from_90
months = 12  * years_from_90
print("You have "+str(days)+" days, "+str(weeks)+" weeks, and "+str(months)+" months left.")
#F-string
print(f"You have {days} days, {weeks} weeks, and {months} months left.")
#Math opetators
#division /: is always a float unless round or assign type int
# ** exponent
# PEMDAS Applyies  Left to right 
#// Floor divission rounds the result into int 

#Fsring
