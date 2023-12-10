A = input()
B = input()
check = A[0:3] == str("DIS") or B[0:3] == str("DIS")
if check:
    print("Discount")
else:
    print("No Discount")