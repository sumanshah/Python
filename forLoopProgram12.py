word = "Pencil"
result = ""

for i in range(len(word)):
    if(i == len(word)-1):
        result = result + word[i]
    else:
        result = result + word[i] + " "

print(result)