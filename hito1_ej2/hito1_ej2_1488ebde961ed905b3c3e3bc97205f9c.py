#Contestador de cel
Numero = input("ponga numero telefonico:")
Hora = int (input("ponga hora de la llamada:"))
if  0 <= Hora <= 7:
    print("si CONTESTAR")
elif Numero[5:] == "909" and Hora < 14:
    print("si CONTESTAR")
elif Numero[0:2] == "887" and 17 <= Hora <= 19:
    print("NO CONTESTAR")

elif Hora > 19:
    print("NO CONTESTAR")
else:
    print("NO CONTESTAR")