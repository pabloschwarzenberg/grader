#Contestador de celular

numero_telefonico = int(input("Ingrese número telefonico: "))
hora = int(input("Ingrese hora de la llamada: "))



if hora <= 7:
    print("Resultado: CONTESTAR")
elif hora>7 and hora <14:
    ultimos_digitos = str(numero_telefonico)[5:]
    if ultimos_digitos=="909":
        print("Resultado: CONTESTAR")
    else:
        print("Resultado: NO CONTESTAR")
elif hora>=17 and hora<=19:
    primeros_digitos = str(numero_telefonico)[:3]
    if primeros_digitos=="877":
        print("Resultado: NO CONTESTAR")
    else:
        print("Resultado: CONTESTAR")
else:
    print("Resultado: NO CONTESTAR")