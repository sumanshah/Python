N = input()
P = len(N)
sum = 0
for i in range(P):
    A = int(N[i]) ** P
    sum = sum + A
print(sum)
if sum == int(N):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")