A = int(input())
B = int(input())
C = A > 300 or B > 300
sum = A + B 
if C and sum < 500:
    print("Can team up")
else:
    print("Cannot team up")