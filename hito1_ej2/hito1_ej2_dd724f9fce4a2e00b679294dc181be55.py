def contestar(hora, numero):
    if(hora >= 0 and hora <= 7):
        return "CONTESTAR"
    elif(hora < 14 and str(numero).endswith("909")):
        return "CONTESTAR"
    elif(hora >= 17 and hora <= 19):
        if(str(numero).startswith("877")):
            return "NO CONTESTAR"
        return "CONTESTAR"
    else:
        return "NO CONTESTAR"
    
#Solicitar al usuario
numero = int(input("Ingresa el numero de telefono (8 cifras): "))
hora = int(input("Ingresa la hora (0-23): "))


#Verificar
resultado = contestar(hora, numero)

#Mostras salida
print(resultado)