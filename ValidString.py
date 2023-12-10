S = input()
Slen = len(S)
P = Slen >= 2 and Slen <= 7
Q = S[0] != str("a") 
if P or Q:
    print("Valid String")
else:
    print("Not a Valid String")