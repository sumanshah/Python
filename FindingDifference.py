a = int(input())
b = int(input())

absolute_difference = a - b 
if absolute_difference < 0:
    absolute_difference = (-1 * (absolute_difference))
    print(absolute_difference)
else:
    print(absolute_difference)
