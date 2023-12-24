word = input()
l_word = len(word)
sum = ""

for i in range(l_word):
    sum = sum + word[i] + "-" 
print(sum[:-1])