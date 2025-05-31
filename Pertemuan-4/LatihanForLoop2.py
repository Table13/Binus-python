userInput = int(input("berapa tinggi segitiga anda: "))
k = userInput - userInput + 2
l = userInput - 1

for i in range(userInput):
    print(str(userInput)*userInput)
    userInput -=1

for i in range(l):
    print(str(k)*k)
    k+=1
