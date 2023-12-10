A = int(input())
B = int(input())
Abet = A > 40 and A < 140
Bbet = B > 40 and B < 140
if Abet or Bbet:
    print("Between 40 and 140: Yes")
else:
    print("Between 40 and 140: No")