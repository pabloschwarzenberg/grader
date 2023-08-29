#Contestador de celular
numero = int(input("Ingrese numero telefonico: "))
hora = int(input("Ingrese Hora de la llamada: "))
revisarnumero = str(numero)

if hora <= 7:
    print ("CONTESTAR")

if 7<hora<=14 and revisarnumero[5:8] != "909":
    print("NO CONTESTAR")
if 7<hora<=14 and revisarnumero[5:8] == "909":
    print("CONTESTAR")

if 14<hora<=17:
    print("NO CONTESTAR")
if 17<hora<=19 and revisarnumero[0:3]!= "877":
    print ("CONTESTAR")
if 17<hora<=19 and revisarnumero[0:3]== "877":
    print ("NO CONTESTAR")
if hora > 19:
    print("NO CONTESTAR")
