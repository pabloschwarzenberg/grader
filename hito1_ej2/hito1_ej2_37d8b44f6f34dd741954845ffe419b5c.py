#Contestador de celular
numFono = int(input("Ingrese el número de telefono ->"))

fono = str(numFono)
num909 = fono[5:8]
contestar909 = int(num909)
num877 = fono[0:3]
Nocontestar877 = int(num877)

hora = int(input("Ingrese la hora de la llamada ->"))
if hora >= 0 and hora <= 7:
    print("Contestar")


if hora > 7 and hora < 14 and contestar909 == 909:
    print("Contestar")
else:
    if hora > 7 and hora < 14 and contestar909 != 909:
        print("No contestar")

    
if hora >= 17 and hora <= 19 and Nocontestar877 == 877:
    print("No contestar")
else:
    if hora >= 17 and hora <= 19 and Nocontestar877 != 877:
        print("Contestar")
        
if hora >= 19:
    print("No contestar")      