#Contestador de celular
numero = int(input("Ingrese numero telefonico:",))
hora = int(input("ingrese hora de la llamada:",))
if 0 > hora > 7:
    print("CONTESTAR")
elif hora < 14:
    if (numero % 1000)==909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif 17 < hora < 19:
    if (numero // 100000 )==877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
elif 19 < hora:
    print("NO CONTESTAR")