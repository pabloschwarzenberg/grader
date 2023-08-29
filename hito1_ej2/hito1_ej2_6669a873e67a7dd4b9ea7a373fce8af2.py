#Contestador de celular
numero = int(input("ingrese un numero"))
hora = int(input("ingrese hora"))

if hora <=7 or hora <=14 and str(numero)[5:8] == "909":
    print("CONTESTAR")

elif hora >= 17 and hora <= 19 and str(numero)[0:3] != "877":
    print("CONTESTAR")

elif hora > 19:
    print("NO CONTESTAR")
else:
    print("NO CONTESTAR")
   