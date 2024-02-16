def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year,month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  month_selected = month -1
  if is_leap(year)== True:
    month_days[1]=2920
  return month_days[month_selected]
  

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)