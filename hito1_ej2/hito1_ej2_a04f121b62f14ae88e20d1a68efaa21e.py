#Contestador de celular
Num=int(input("Ingrese un número de 8 cifras: "))
Hora=int(input("Ingrese una hora (0 a 23): "))

if Hora>=0 and Hora<=7:
    print("CONTESTAR")
elif Hora>7 and Hora<14 and (Num%(10**3))==909:
    print("CONTESTAR")
elif Hora>=17 and Hora<=19:
    if (Num//(10**5))==877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
elif Hora>19 and Hora<=23:
    print("NO CONTESTAR")
