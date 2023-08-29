#Contestador de celular
numero=int(input("Ingrese numero telefonico (8 digitos):"))
hora=int(input("Ingrese hora de llamada(0-24):"))
numeroStart=numero//100000
numeroEnd=numero%1000
if hora>0 and hora<7:
    print("CONTESTAR")
elif hora<14:
    if numeroEnd==909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif hora==18:
    if numeroStart==877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
else:
    hora>19
    print("NO CONTESTAR")