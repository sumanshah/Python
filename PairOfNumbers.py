A = int(input())
B = int(input())
D = A <= 1000 and B <= 1000
if D or B > 500:
    print("Pair")
else:
    print("Not a Pair")