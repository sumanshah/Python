A = int(input()) 
B = int(input())
A_power_B = A**B 
B_power_A = B**A 
if A_power_B > B_power_A:
    print(A_power_B)
else:
    print(B_power_A)