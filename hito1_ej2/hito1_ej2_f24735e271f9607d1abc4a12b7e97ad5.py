#Contestador de celular
numero = int(input("Ingrese el número de teléfono (8 cifras): "))
hora = int(input("Ingrese la hora del día (0-23): "))
if hora >= 0 and hora <= 7:
    respuesta = "CONTESTAR"  
elif hora < 14 and (numero % 1000) == 909:
    respuesta = "CONTESTAR"  
elif hora >= 17 and hora <= 19 and (numero // 1000000) == 877:
    respuesta = "CONTESTAR" 
else:
    respuesta = "NO CONTESTAR" 


print(respuesta)      