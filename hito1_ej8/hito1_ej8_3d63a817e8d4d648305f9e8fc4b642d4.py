#Descomponer un número
#Entradas
num = int(input("Ingrese un número de 4 dígitos: "))

#Evaluación 
mil = int(num // 1000)
cen = int(num//100 - mil*10)
dec = int(num//10 - (mil*100 + cen*10))
uni = int(num - (mil*1000 + cen*100 + dec*10))

#Verificar la cantidad de dígitos:
if num <= 9999:
    if mil > 0:
        mil = str(mil)
        cen = str(cen)
        dec = str(dec)
        uni = str(uni)
        print(mil + "M +", cen + "C +", dec + "D +", uni + "U.")
    elif cen > 0:
        cen = str(cen)
        dec = str(dec)
        uni = str(uni)
        print(cen + "C +", dec + "D +", uni + "U.")
    elif dec > 0:
        dec = str(dec)
        uni = str(uni)
        print(dec + "D +", uni + "U.")
    elif uni > 0:
        uni = str(uni)
        print(uni + "U.")
    else:
        print("0U")
else:
    print("El número ingresado tiene mas de 4 dígitos.")