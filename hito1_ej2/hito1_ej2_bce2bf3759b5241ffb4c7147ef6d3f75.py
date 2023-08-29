#Contestador de celular
def contestar_celular(hora, numero):
    if hora >= 0 and hora <= 7:
        return True
    elif hora < 14 and numero % 100 == 909:
        return True
    elif hora >= 17 and hora <= 19 and numero // 1000000 == 877:
        return False
    else:
        return False

# Solicitar al usuario la hora y el número de teléfono
hora_llamada = int(input("Ingrese la hora de la llamada (0-23): "))
numero_telefono = int(input("Ingrese el número de teléfono (8 dígitos): "))

# Determinar si debes contestar o no el celular
debes_contestar = contestar_celular(hora_llamada, numero_telefono)

# Imprimir la respuesta
if debes_contestar:
    print("Debes contestar el celular.")
else:
    print("No debes contestar el celular.")
