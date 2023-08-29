#Contestador de celular
numero = str(input("Ingrese el número de teléfono (8 dígitos): "))
hora = int(input("Ingrese la hora (0-23): "))

if 0 <= hora <= 7:
    print("CONTESTAR")
    

elif hora < 14 and numero[5] + numero[6] + numero[7] == "909":
    print("CONTESTAR")  

elif 17 <= hora <= 19 and numero[0] + numero[1] + numero[2] != "877":
    print("CONTESTAR")
    

elif hora >= 19:
    print("NO CONTESTAR")
    

else:
    print("NO CONTESTAR")
