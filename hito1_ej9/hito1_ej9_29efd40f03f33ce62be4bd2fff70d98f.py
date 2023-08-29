#Sistema de Ecuaciones
num1 = eval(input("Ingrese número 1 de la primera ecuación: "))
num2 = eval(input("Ingrese número 2 de la primera ecuación: "))
num3 = eval(input("Ingrese número 3 de la primera ecuación: "))

numA = eval(input("Ingrese número A de la segunda ecuación: "))
numB = eval(input("Ingrese número B de la segunda ecuación: "))
numC = eval(input("Ingrese número C de la segunda ecuación: "))

numA1 = numA * num1
numA2 = numA * num2
numA3 = numA * num3

numAA1 = (-1 * num1) * numA
numBB1 = (-1 * num1) * numB
numCC1 = (-1 * num1) * numC


Y = (numA3 + numCC1)/(numA2 + numBB1)
X = numC - (numB * Y)

print("x=",round(X,1))
print("y=",round(Y,1))
