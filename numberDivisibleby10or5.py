number = int(input())
is_divisible_10 = ((number % 10) == 0)
is_divisible_5 = ((number % 5) == 0)

if is_divisible_10:
    print("Number Divisible by 10")
elif is_divisible_5:
    print("Number Divisible by 5")
else:
    print("Number is not Divisible by 10 or 5")