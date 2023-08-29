#Descomponer un número
num = int(input("Ingrese un numero para descomponerlo: "))

numU = (num%10)

numD = int((num%100) / 10)

numC = int((num%1000) / 100)

numM = int((num%10000) / 1000)

print(numM, "M", "+", numC, "C", "+", numD, "D", "+", numU, "U")