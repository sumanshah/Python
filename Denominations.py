a = int(input())

notes_1000 = 0
notes_500 = 0
notes_100 = 0
notes_50 = 0
notes_20 = 0
notes_10 = 0
notes_5 = 0
notes_1 = 0

if a>=1000:
    notes_1000 = a // 1000
    a = a % 1000

if a>= 500:
    notes_500 = a // 500
    a = a % 500

if a>= 100:
    notes_100 = a // 100
    a = a % 100

if a>= 50:
    notes_50 = a // 50
    a = a%50

if a >= 20:
    notes_20 = a // 20
    a = a % 20

if a >= 10:
    notes_10 = a // 10
    a = a%10

if a >= 5:
    notes_20 = a // 5
    a = a % 5

if a >= 1:
    notes_10 = a // 1
    a = a%1

print("1000 : " + str(notes_1000))
print("500 : " + str(notes_500))
print("100 : " + str(notes_100))
print("50 : " + str(notes_50))
print("20 : " + str(notes_20))
print("10 : " + str(notes_10))
print("5 : " + str(notes_5))
print("1 : " + str(notes_1))
