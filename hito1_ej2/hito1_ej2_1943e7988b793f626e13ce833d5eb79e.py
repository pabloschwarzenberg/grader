#Contestador de celular
numero = 0
hora = -1
while len(str(numero)) != 8:
    numero = int(input("Ingrese el numero telefónico de 8 digitos : "))
while hora<0 or hora>23:
    hora=int(input("Ingrese hora de la llamada en formato de 00 a 24 : "))
if hora >= 0 and hora < 7:
    print("CONTESTAR")
elif hora >= 7 and hora < 14:
    if str(numero)[5:] == "909":
        print("Contestar")
    else:
        print("No contestar")
elif hora >= 14 and hora < 17:
    if str(numero)[0:3] == "877":
        print("Contestar")
    else:
        print("No contestar")
elif hora >= 17 and hora < 19:
    if str(numero)[0:3] == "877":
        print("No contestar")
    else:
        print("Contestar")
elif hora >= 19 and hora < 23:
    print("No contestar")
 