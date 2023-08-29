#Ordenar tres números
numA= int(input("ingrese el primer numero: "))
numB= int(input("ingrese el segundo numero: "))
numC= int(input("ingrese el tercer numero: "))
if (numA >= numB) and (numB >= numC):
    print(numC,",",numB,",",numA)

elif (numA<= numB) and (numB<=numC):
    print(numA,",",numB,",",numC)

elif (numA>=numB) and (numB<=numC) and (numA>=numC):
    print(numB,",",numC,",",numA)

elif (numA>=numB) and (numB<=numC) and (numA<=numC):
    print(numB,",",numA,",",numC)

elif (numA<=numB) and (numB>=numC) and (numA>=numC):
    print(numC,",",numA,",",numB)

elif (numA<=numB) and (numB>=numC) and (numA<=numC):
    print(numA,",",numC,",",numB)