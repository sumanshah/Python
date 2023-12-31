N = input()
Nl = len(N)
sum = ""
for i in range(Nl):
    sum = sum + N[Nl-1]
    Nl = Nl - 1

print(sum)