#Contestador de celular
def contestar_celular(hora, numero):
    if hora >= 0 and hora < 7:
        return True  # Contestar entre 00:00 y 07:00 (posible emergencia)
    elif hora < 14 and numero % 100 == 909:
        return True  # Contestar antes de las 14:00 si el número termina en 909
    elif hora >= 17 and hora < 19 and str(numero).startswith("877"):
        return True  # Contestar entre 17:00 y 19:00 si el número comienza por 877
    else:
        return False  # No contestar 

# Solicitar la hora y el número al usuario
hora_llamada = int(input("Ingrese la hora de la llamada (0-23): "))
numero_telefonico = int(input("Ingrese el número telefónico (8 dígitos): "))

# Determinar si se contesta automáticamente el celular o no
contestar = contestar_celular(hora_llamada, numero_telefonico)
if contestar:
    print("Contestar automáticamente el celular.")
else:
    print("No contestar el celular.")
      