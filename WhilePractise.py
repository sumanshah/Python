m = 16
sum = 0
while m <= 14:
    if(m % 2) == 0:
        sum = sum + 1
    if(m % 5) == 0:
        sum = sum + 2
    m = m + 1

print(sum)