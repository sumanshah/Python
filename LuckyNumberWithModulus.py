number = int(input())
remainder = number % 9
multiple_of_9 = remainder == 0

number = str(number)
first_digit = int(number[0])
second_digit = int(number[1])

is_first_digit_9 = first_digit == 9
is_second_digit_9 = second_digit == 9

is_any_digit_9 = is_first_digit_9 or is_second_digit_9

if is_any_digit_9 or multiple_of_9:
    print("Lucky Number")
else:
    print("Unlucky Number")