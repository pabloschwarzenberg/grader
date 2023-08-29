#Contestador de celular
numero = str(input("Ingrese numero telefonico:")
time = str(input("Ingrese hora de la llamada:")
if time > 0 and time < 7:
    print("CONTESTAR")
if time > 19 and time <= 23:
    print("NO CONTESTAR")
else:
    if time > 7 and time < 14 and str(numero[-3]) == "9" and str(numero[-2]) ==
        print("CONTESTAR")
    if time > 7 and time < 14 and str(numero[-3]) != "9" and str (numero[-2]) !=
        print("NO CONTESTAR")
    if time > 17 and time < 19 and str(numero[0:1]) == "8" and str(numero[1:2])
        print("NO CONTESTAR")
    if time > 17 and time < 19 and str(numero[0:1]) != "8" and str(numero[1:2])
        print("CONTESTAR")