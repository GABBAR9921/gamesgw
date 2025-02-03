import random

values = [0, 1, -1]
computer = random.choice(values)

# computer = 1

youstr =  input("Enter your choise :")

youDict = {"s":1, "w":-1, "g":0}

you = youDict[youstr]
reversstr = {1:"snack", -1:"water", 0:"gun"}


print("Computer choise is ", reversstr[computer])
print("Your choise is ",reversstr [you])
if (computer ==  you):
    print(" Draw")
elif (computer == -1 and you==1):
    print(" you win ")
elif (computer == -1 and you==0):
    print(" you lose ")
elif (computer == 0 and you==1):
    print(" you win ")
elif (computer == 0 and you==-1):
    print(" you win ")
elif (computer == 1 and you== -1):
    print(" you lose ")
else:
    print("Something went wrong")
