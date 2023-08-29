#Contestador de celular
numero = int(input("Ingrese numero telefonico: "))
hora = int(input("Ingrese hora de llamada: "))

numero = str(numero)

if hora >= 0 and hora <= 7:
    print("CONTESTAR")
elif hora < 14 and numero[5:] == "909":
    print("CONTESTAR")
elif hora >= 17 and hora <= 19 and numero[0:3] != "877":
    print("CONTESTAR")
else:
    print("NO CONTESTAR")      