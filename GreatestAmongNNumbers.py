N = int(input())
A = int(input())

for i in range(N-1):
    B = int(input())
    if  B > A:
        A = B
print(A)
