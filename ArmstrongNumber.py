N = input()
first_N = N[0]
Second_N = N[1]
Third_N = N[2]
Sum_of_cube = (int(N[0]) ** 3) + (int(N[1]) ** 3) + (int(N[2]) ** 3)
if int(N) == Sum_of_cube:
    print("True")
else:
    print("False")