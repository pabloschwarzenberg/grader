#Contestador de celular
numero = int(input("Ingrese numero telefonico: "))
hora = int(input("Ingrese hora de la llamada: "))
contador = 0
if 0 <= hora < 7:
    contador += 1
elif hora < 14:
    if str(numero)[-3:] == "909":
        contador += 1
elif 17 <= hora < 19:
    if str(numero)[:3] != "877":
        contador += 1
if contador > 0:
    print("CONTESTAR")
else:
    print("NO CONTESTAR")
