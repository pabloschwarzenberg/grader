#Descomponer un número
def descomponer(num):
    if len(num) == 4:
        return("%sM + %sC + %sD +%sU"%(num[0],num[1],num[2],num[3]))
    elif len(num) == 3:
        return("%sC + %sD + %sU"%(num[0],num[1],num[2]))
    elif len(num) == 2:
        return("%sD + %sU"%(num[0],num[1]))
    else:
        return("%sU"%(num))

    
numero = input("Ingrese un número de no más de 4 cifras: ")
print(descomponer(numero))