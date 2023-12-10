A = int(input())
B = int(input())
C = A == 6 or B == 6
Sum = (A+B) == 6
Diff = (A-B)==6 or (B-A)==6
if C or Sum or Diff:
    print("Lucky Number")
else:
    print("Not Lucky")