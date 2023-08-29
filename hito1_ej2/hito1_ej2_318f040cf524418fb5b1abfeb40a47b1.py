#Contestador de celular
numeroTelefono = int(input())
while len(str(numeroTelefono)) != 8:
    numeroTelefono = int(input())
hora = int(input())
while hora < 0 or hora > 23:
    hora = int(input())
finalNum = str(numeroTelefono)[-3:]

if hora >= 0 and hora <= 7:
    print("CONTESTAR")
elif hora > 7 and hora < 14:
    if finalNum == "909":
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif hora > 19:
    print("NO CONTESTAR")
elif hora >= 17 and hora <= 19:
    if finalNum == "877":
        print("NO CONTESTAR")
    else:
        print("NO CONTESTAR")
else: print("NO CONTESTAR")