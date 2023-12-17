N = input()
NLen = len(N)
num_square = str(int(N) ** 2)
num_square_len = len(num_square)
last_digit = N[int(NLen) - 1] == num_square[int(num_square_len) - 1]
if last_digit:
    print("Equal")
else:
    print("Not Equal")