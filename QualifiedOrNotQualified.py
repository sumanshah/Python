M = int(input())
P = int(input())
A = M > 35 and P > 35
B = M + P >= 100
if A or B:
    print("Qualified")
else:
    print("Not Qualified")