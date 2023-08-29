#Cálculo del dígito verificador de un rut
rut=(input("ingrese rut sin puntos ni el ultimo numero despues del guión: "))
arut=str(rut)
num=len(arut)
if(num==8):
    uno=(int(rut[7])) * 2
    dos=(int(rut[6])) * 3
    tres=(int(rut[5])) * 4
    cuatro=(int(rut[4])) * 5
    cinco=(int(rut[3])) * 6
    seis=(int(rut[2])) * 7
    siete=(int(rut[1])) * 2
    ocho=(int(rut[0])) * 3
    suma = uno + dos + tres + cuatro + cinco + seis + siete + ocho
    numT=suma//11
    resto=suma-(11 * numT)
    resultado=11-resto

    if (resultado==11):
        print("dv=0")
    elif (resultado == 10):
        print("dv=k")
    else:
        print("dv={}".format(resultado))

if (num==7):
    uno=(int(rut[6])) * 2
    dos=(int(rut[5])) * 3
    tres=(int(rut[4])) * 4
    cuatro=(int(rut[3])) * 5
    cinco=(int(rut[2])) * 6
    seis=(int(rut[1])) * 7
    siete=(int(rut[0])) * 2
    suma = uno + dos + tres + cuatro + cinco + seis + siete
    numT=suma//11
    resto=suma-(11*numT)
    resultado=11-resto

    if (resultado==11):
        print("dv=0")
    elif (resultado==10):
        print("dv=k")
    else:
        print("dv={}".format(resultado))