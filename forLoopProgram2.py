start_num = 10
end_num = 20
total = 0

for i in range(start_num, end_num):
    if(i%5) == 0:
        total = total + i

print(total)