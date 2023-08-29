numero = input("Cual es tu numero telefonico?:")
hora = int (input("A que hora es tu llamada?:"))
if  0 <= hora <= 7:
    print("CONTESTAR")
elif numero[5:] == "909" and hora < 14:
    print("CONTESTAR")
elif numero[0:2] == "887" and 17 <= hora <= 19:
    print("NO CONTESTAR")

elif hora > 19:
    print("NO CONTESTAR")
else:
    print("NO CONTESTAR")    