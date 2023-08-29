#Descomponer un número

#ENTRADA

NUM= int(input("Ingrese un número de hasta 4 dígitos: "))

#DESARROLLO

if NUM <= 9999:
    MIL = NUM // 1000
    RES = NUM - (MIL * 1000)
    CEN = RES // 100
    RES = RES - (CEN * 100)
    DEC = RES // 10
    UNI = RES - (DEC * 10)

#SALIDA

    print( str(MIL) + "M +" + str(CEN) + "C +" + str(DEC) + "D +" + str(UNI) + "U " )
else:
    print("error, tiene más de 4 digitos")
