#Contestador de celular
numero = input("Ingrese número telefónico: ")
hora = int(input("Ingrese hora de la llamada (0-23): "))

if hora >= 0 and hora <= 7:
    print("Resultado: CONTESTAR")
elif hora < 14 and numero.endswith("909"):
    print("Resultado: CONTESTAR")
elif hora >= 17 and hora <= 19 and numero.endswith("877"):
    print("Resultado: CONTESTAR")
else:
    print("Resultado: NO CONTESTAR")
