N = int(input())
M = int(input())
count = 0
sum = 0

while count < M:
    sum = sum + N
    N = N + 1
    count = count + 1

print(sum)