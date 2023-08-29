#Contestador de celular

numero = int(input("Ingrese numero telefonico: "))
hora = int(input("Ingrese hora de la llamada entre 0 y 23: "))

if hora > 0 and hora < 7:
    print("CONTESTAR.")
elif hora >= 7 and hora < 14:
    if numero % 100 == 909:
        print("CONTESTAR.")
    else:
        print("NO CONTESTAR.")
elif hora >= 17 and hora <= 19:
    if numero // 1000000 == 877:
        print("CONTESTAR.")
    else:
        print("NO CONTESTAR.")
else:
    print("NO CONTESTAR.")