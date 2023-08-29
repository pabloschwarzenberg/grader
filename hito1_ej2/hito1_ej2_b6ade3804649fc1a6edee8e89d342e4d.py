#Contestador de celular

def contestar_llamada(hora, numero):
    if hora >= 0 and hora < 7:
        return "CONTESTAR"  # Contestar en caso de emergencia (00:00 - 07:00)
    elif hora < 14 and numero % 100 == 909:
        return "CONTESTAR"  # Contestar si el número termina en 909 (antes de las 14:00)
    elif hora >= 17 and hora < 19 and str(numero).startswith("877"):
        return "NO CONTESTAR"  # No contestar si el número comienza por 877 (17:00 - 19:00)
    else:
        return "NO CONTESTAR"  # No contestar en cualquier otro caso

# Obtener los datos del usuario
numero_telefono = int(input("Ingrese número telefónico: "))
hora_llamada = int(input("Ingrese hora de la llamada (0-23): "))

# Verificar si contestar o no
resultado = contestar_llamada(hora_llamada, numero_telefono)

# Mostrar el resultado
print("Resultado:", resultado)
