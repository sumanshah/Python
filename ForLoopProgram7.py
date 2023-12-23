word = "Home Work"
length_of_word = len(word)
for i in range(length_of_word):
    if word[i] == " ":
        print(word[:i])