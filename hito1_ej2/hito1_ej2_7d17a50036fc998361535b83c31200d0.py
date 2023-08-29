#Contestador de celular
hora = int(input("Ingrese la hora (0-23): "))
numero = int(input("Ingrese el número de celular (8 dígitos): "))

if hora >= 0 and hora < 7:
    print("CONTESTAR")
if hora < 14 and numero % 1000 == 909:
    print("CONTESTAR")
elif hora >= 17 and hora <= 19: 
    print("CONTESTAR")
elif hora >= 17 and hora <= 19 and numero // 10000000 == 877:
    print("NO CONTESTAR")
else:
    print("NO CONTESTAR")      