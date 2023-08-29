#Contestador de celular
numero = int(input("Ingrese numero de celular: "))
hora = int(input("Ingrese hora de llamada: "))

if hora >= 0 and hora <= 7:
    print("Contestar")

elif hora < 14 and str(numero).endswith("909"):
    print("Contestar")

elif hora >= 17 and hora <= 19 and str(numero).startswith("877"):
    print("No contestar")

else:
    print("No contestar")