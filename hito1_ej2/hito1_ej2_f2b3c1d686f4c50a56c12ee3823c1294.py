#Contestador de celular
numero = int(input("Ingrese el numero telefonico:"))
hora = int(input("Ingrese la hora de la llamada:"))


if hora >= 0 and hora <= 7:
    print("CONTESTAR")
else:
    hora >= 8 and hora <= 12
    if numero % 1000 != 909:
         print("NO CONTESTAR")
    if numero % 1000 == 909:
        print("CONTESTAR")
if hora == 14 and hora < 17:
    print("NO CONTESTAR")
elif hora == 17 and hora <= 19:
    if numero % 10000000 != 877:
        print("CONTESTAR")
    if numero % 10000000 == 877:
        print("NO CONTESTAR")
elif hora > 19 and hora < 23:
        print("NO CONTESTAR")