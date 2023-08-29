#Contestador de celular
Numero = input("introduzca Numero telefonico:")
Hora = int (input("coloque Hora de la llamada:"))
if  0 <= Hora <= 7:
    print("CONTESTAR")
elif Numero[5:] == "909" and Hora < 14:
    print("CONTESTAR")
elif Numero[0:2] == "887" and 17 <= Hora <= 19:
    print("NO CONTESTAR")

elif Hora > 19:
    print("NO CONTESTAR")
else:
    print("NO CONTESTAR")    