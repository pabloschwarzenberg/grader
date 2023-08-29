#Contestador de celular
numero = int(input("ingrese numero telefonico: "))
hora = int(input("ingrese hora de la llamada: "))
numero = str(numero)
if hora >= 0 and hora <= 7:
    print("CONTESTAR")
elif hora >= 8 and hora <= 14 and numero[5:8] == "909": 
    print("CONTESTAR")
elif hora >= 17 and hora <=19 and numero[0:3] != "877":
    print("CONTSTAR")
elif hora >=19 and hora <= 23:
    print( "NO CONTESTAR")
else:
    print("NO CONTESTAR")
