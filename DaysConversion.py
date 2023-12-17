a = int(input())

one_year = 365
one_week = 7

b = a % one_year
days = b % one_week
years = a // one_year 
weeks = b // one_week 

print(str(years) + " years " + str(weeks) + " weeks " + str(days) + " days ")

