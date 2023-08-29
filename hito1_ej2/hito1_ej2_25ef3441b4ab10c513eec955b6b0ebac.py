#Contestador de celular
Numero=int(input("Ingrese el número de teléfono (8 digitos): "))
Hora=int(input("Ingrese la hora (Entre 0 y 23): "))
C="CONTESTAR"
NC="NO CONTESTAR"
excepcion1=str(909)
excepcion2=str(877)
cadena=str(Numero)
if Hora>=0 and Hora<=7:
    print(C)
if Hora>7 and Hora<14:
    if cadena[5]+cadena[6]+cadena[7]==excepcion1:
        print(C)
    else:
        print(NC)
if Hora>=14 and Hora<17:
    print(NC)
if Hora>=17 and Hora<=19:
    if cadena[0]+cadena[1]+cadena[2]==excepcion2:
        print(NC)
    else:
        print(C)
if Hora>19 and Hora<=23:
    print(NC)