#Contestador de celular
numero=int(input("introduza los 8 digitos del numero de telefeno: "))
hora=int(input("introduzca la hora de la llamada: "))


if  hora>=0 and hora<7:
    print("CONTESTAR  ES UNA LLAMADA DE EMERGENCIA")
if  hora>=7 and hora<14 :
    if numero%1000==909:
        print("CONTESTAR")
    else:
            print("NO CONTESTAR")
if hora>=17 and hora<=19:
    if numero//1000==877:
        print("CONTESTAR")
    else:
          print("NO CONTESTAR")
if hora>=20 and hora<=23 :
    print("NO CONTESTAR")
if hora>=14 and hora<17:
    print("NO CONTESTAR")      