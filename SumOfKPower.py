N = int(input())
K = int(input())
sum = 0
for i in range(1, N+1):
    sum = sum + (i ** K)
print(sum)