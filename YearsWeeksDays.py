N = int(input())
years = N // 365
print(years)
remainder_1 = years * 365
remainder_2 = N - remainder_1
weeks = remainder_2 // 7
remainder_3 = weeks * 7
remainder_4 = remainder_2 - remainder_3
print(weeks)
print(remainder_4)