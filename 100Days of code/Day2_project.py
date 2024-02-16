
Bill   = float(input("Welcome to the tip calculator.\nWhat was the total bill? $ "))
Tip    = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
tip_deci = int(Tip)/100
Tip_amount = Bill*tip_deci
total  = Bill+Tip_amount
num_split = int(input("how many people to split the bill? "))
per_person = round(total/num_split,2)
#per_person = {:.2f}.format(per_person)
print(f"each person should pay: ${per_person}")
