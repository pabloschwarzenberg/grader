#Descomponer un número
num = input("Ingresa un numero de 4 digitos: \n")
cont = 0
numf = []

for i in num[::-1]:
    cont += 1
    if cont == 1:
        numf.append(str(i) + "U")
    elif cont == 2:
        numf.append(str(i) + "D + ")
    elif cont == 3:
        numf.append(str(i) + "C +")
    elif cont == 4:
        numf.append(str(i) + "M +")
numd = reversed(numf)
print(*numd)

