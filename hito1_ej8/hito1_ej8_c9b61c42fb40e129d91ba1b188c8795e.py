#Descomponer un número
nro = int(input("Ingrese un numero: "))
while not(nro>0 and nro<=9999):
    nro = int(input("Ingrese otro número: "))
nroCod = str(nro)
largo = len(nroCod)
if (largo == 1):
    uni = nroCod[0]
    print(str(uni +"U"))
elif (largo == 2):
    dec = nroCod[0]
    uni = nroCod[1]
    print(str(dec + "D"),"+",str(uni + "U"))
elif (largo == 3):
    cen = nroCod[0]
    dec = nroCod[1]
    uni = nroCod[2]
    print(str(cen + "C"),"+",str(dec + "D"),"+",str(uni + "U"))
else:
    mil = nroCod[0]
    cen = nroCod[1]
    dec = nroCod[2]
    uni = nroCod[3]
    print(str(mil + "M"),"+",str(cen + "C"),"+",str(dec + "D"),"+",str(uni + "U"))      