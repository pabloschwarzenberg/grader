#Contestador de celular
Num = int(input("Ingrese numero telefonico:"))
Hor = int(input("Ingrese hora de la llamada:"))
      
if 0 <= Hor <= 7:
    print("CONTESTAR")

if 7 < Hor < 14:
    if str(Num)[5:8] == "909":
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")

if 14 <= Hor < 17:
     print("NO CONTESTAR")

if 17 <= Hor <= 19:
    if str(Num)[0:3] == "877":
        print("NO CONTESTAR")
    else: 
        print("CONTESTAR")

if 19 < Hor <= 23:
    print("NO CONTESTAR")