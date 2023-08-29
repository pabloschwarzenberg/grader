#Descomponer un numero!!!!
#Descomponer un número
print("-----------------")
numeros = int(input("Numero "))
numeros = str(numeros)
M = numeros[0:4]
C = numeros[0:3]
D = numeros[0:2]
U = numeros[0:1]
if (numeros == M) and not (numeros == C) and not (numeros == D) and not (numeros == U):
    print(numeros[0:1] + "M+" + numeros[1:2] + "C+" + numeros[2:3] + "D+" + numeros[3:4] + "U")
elif (numeros == C) and not (numeros == D) and not (numeros == U):
    print(numeros[0:1] + "C+" + numeros[1:2] + "D+" + numeros[2:3] + "U")
elif (numeros == D) and not (numeros == U):
    print(numeros[0:1] + "D+" + numeros[1:2] + "U")
elif (numeros == U):
    print(numeros[0:1] + "U")