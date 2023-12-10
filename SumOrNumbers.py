A = int(input())
B = int(input())
Les = A < 20 or B < 20
sum = A + B > 30 and A + B < 50
if Les or sum :
    print(A+B)
else:
    print(A)
    print(B)