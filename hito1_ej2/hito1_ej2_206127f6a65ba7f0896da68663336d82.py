#Contestador celular
numero = input("Ingrese un número telefónico: ")
hora = int(input("Ingrese la hora de la llamada: "))

if hora >= 0 and hora <= 7:
    print("Resultado: CONTESTAR")
elif hora < 14:
    if numero.endswith("909"):
        print("Resultado: CONTESTAR")
    else:
        print("Resultado: NO CONTESTAR")
elif hora >= 17 and hora <= 19:
    if numero.startswith("877"):
        print("Resultado: NO CONTESTAR")
    else:
        print("Resultado: CONTESTAR")
else:
    print("Resultado: NO CONTESTAR")