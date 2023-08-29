def contestar_llamada(numero, hora):
    numero = int(numero)
    hora = int(hora)
    
    if hora >= 0 and hora < 7:
        return "CONTESTAR"
    elif hora < 14:
        if str(numero)[-3:] == '909':
            return "CONTESTAR"
        else:
            return "NO CONTESTAR"
    elif hora >= 17 and hora < 19:
        if str(numero).startswith('877'):
            return "NO CONTESTAR"
        else:
            return "NO CONTESTAR"
    else:
        return "NO CONTESTAR"

# Ejemplo de uso
numero_telefonico = input("Ingrese número telefónico: ")
hora_llamada = input("Ingrese hora de la llamada (entre 0 y 23): ")

resultado = contestar_llamada(numero_telefonico, hora_llamada)
print("Resultado:", resultado)
