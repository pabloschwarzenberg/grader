# Contestador de celular
def contestar_celular(numero_telefonico, hora_llamada):
    if hora_llamada >= 0 and hora_llamada <= 7:
        return "contestar"
    elif hora_llamada < 14 and numero_telefonico % 100 == 909:
        return "contestar"
    else:
        return "no contestar"
         
numero_telefonico = int(input("Ingrese el número telefónico (8 cifras): "))
hora_llamada = int(input("Ingrese la hora de llamada (0-23): "))

resultado = contestar_celular(numero_telefonico, hora_llamada)

print("Resultado:", resultado)