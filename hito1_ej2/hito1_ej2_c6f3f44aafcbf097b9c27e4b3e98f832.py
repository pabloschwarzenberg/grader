#Contestador de celular
Nro = input("ponga nro telefonico:")
Hr = int (input("ponga hr de la llamada:"))
if  0 <= Hr <= 7:
    print("CONTESTAR")
elif Nro[5:] == "909" and Hr < 14:
    print("CONTESTAR")
elif Nro[0:2] == "887" and 17 <= Hr <= 19:
    print("NO CONTESTAR")

elif Hr > 19:
    print("NO CONTESTAR")
else:
    print("NO CONTESTAR")      