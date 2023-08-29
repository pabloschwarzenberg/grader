#Contestador de celular
def contestar_llamada(hora, numero_telefonico):
    if hora >= 0 and hora <= 7:
        
        return "CONTESTAR"
    elif hora < 14 and numero_telefonico % 100 == 909:
        
        return "CONTESTAR"
    elif hora >= 17 and hora <= 19 and numero_telefonico // 1000000 == 877:
        
        return "CONTESTAR"
    else:
        
        return "NO CONTESTAR"


numero_telefonico = int(input("Ingrese el número telefónico (8 dígitos): "))
hora_llamada = int(input("Ingrese la hora de la llamada (0-23): "))


resultado = contestar_llamada(hora_llamada, numero_telefonico)


print("Resultado:", resultado)
