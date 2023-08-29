#Entrada
numero = str(input("Ingrese El Numero Telefonico: "))
hora = int(input("Ingrese La Hora: "))
digitos_finales = numero[5:]
primeros_digitos = numero[0:3]
#Proceso
if hora >= 0 and hora <= 7:
    print("CONTESTAR")
elif (hora >= 0 and hora <=13) and digitos_finales == "909":
    print("CONTESTAR")
elif (hora >= 17 and hora <= 19 ) and primeros_digitos != "877":
    print ("CONTESTAR")
elif hora > 19:
    print("NO CONTESTAR")
else:
    print("NO CONTESTAR")