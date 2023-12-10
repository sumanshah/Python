N = input()
A = N[0] != "5" or N[1] != "5" or N[2] != "5"
B = int(N) > 300 and int(N) < 700
if A and B:
    print("Valid Number")
else:
    print("Not a Valid Number")