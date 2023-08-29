#Descomponer un número
num = int(input("Numero "))
num = str(num)
M = num[0:4]
C = num[0:3]
D = num[0:2]
U = num[0:1]
if (num == M) and not (num == C) and not (num == D) and not (num == U):
    print(num[0:1] + "M+" + num[1:2] + "C+" + num[2:3] + "D+" + num[3:4] + "U")
elif (num == C) and not (num == D) and not (num == U):
    print(num[0:1] + "C+" + num[1:2] + "D+" + num[2:3] + "U")
elif (num == D) and not (num == U):
    print(num[0:1] + "D+" + num[1:2] + "U")
elif (num == U):
    print(num[0:1] + "U")