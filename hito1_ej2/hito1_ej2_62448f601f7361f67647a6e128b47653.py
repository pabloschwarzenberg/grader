#Contestador de celular
numero = str(input("Ingrese el número telefónico: "))
hora = int(input("Ingrese hora de la llamada: "))

if hora > 0 and hora < 7:
    print("CONTESTAR")
elif hora > 7 and hora <= 14:
    if str(numero[-3]) == "9" and str(numero[-2]) == "0" and str(numero[-1]) == "9":
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif hora > 17 and hora <= 19:
    if str(numero[-8]) == "8" and str(numero[-7]) == "7" and str(numero[-6]) == "7":
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
elif hora > 19 and hora <=23:
    print("NO CONTESTAR")




