#Descomponer un número
print("Introduzca un número:")
numero1 = int(input())
M = numero1/1000
n = numero1%1000
C = n/100
n = n%100
D= n/10
U= n%10
if M==range(1,10):
    print("+%iC"%C,"+%iD"%D,"+%iU" % U)
else:
    print("%iM" % M,"+%iC"%C,"+%iD"%D,"+%iU" % U)   