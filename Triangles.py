A = int(input())
B = int(input())
C = int(input())

if ( A == B and A == C and B == C):
    print("Equilateral Triangle")
elif(A == B or B == C or A == C):
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")