#Contestador de celular
def contestar_llamada(hora, numero):
    if hora >= 0 and hora < 7:
        return "CONTESTAR" 
    elif hora < 14 and numero % 100 == 909:
        return "CONTESTAR"  
    elif hora >= 17 and hora < 19 and numero // 10000000 == 877:
        return "CONTESTAR"  
    else:
        return "NO CONTESTAR"  

hora = int(input("Ingrese la hora (0-23): "))
numero = int(input("Ingrese el número de celular (8 cifras): "))

respuesta = contestar_llamada(hora, numero)
print(respuesta)      