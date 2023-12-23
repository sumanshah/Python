verb = "Run"
result = ""

for i in range(len(verb)):
    if(i==len(verb) - 1):
        result = result + verb[i]
    else:
        result = result + verb[i] + " "

print(result)