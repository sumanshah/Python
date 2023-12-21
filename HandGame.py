a = input()
b = input()

if ( a== "Rock" and b == "Scissor") or (a == "Paper" and b == "Scissor") or ( a== "Paper" and b == "Rock"):
    print("Abhinav Wins")
elif(a == "Paper" and b == "Paper") or (a == "Rock" and b == "Rock") or (a == "Scissor" and b == "Scissor"):
    print("Its a Tie")
else:
    print("Anjali Wins")