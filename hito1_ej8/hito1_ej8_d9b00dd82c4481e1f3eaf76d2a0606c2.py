#Descomponer un número
num = int(input("Introduzca un número: "))

M = num / 1000
tmp = num % 1000

C = tmp / 100
tmp = tmp % 100

D= tmp / 10
U= tmp % 10

if M==range(1,10):
    print("+%iC"%C,"+%iD"%D,"+%iU" % U)
else:
    print("%iM" % M,"+%iC"%C,"+%iD"%D,"+%iU" % U)      