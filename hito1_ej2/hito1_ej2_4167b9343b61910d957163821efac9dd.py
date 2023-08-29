#Contestador de celular
def contestar_celular(numero_telefonico, hora_llamada):
    if hora_llamada >= 0 and hora_llamada <= 7:
        print("CONTESTAR")
    elif hora_llamada < 14 and numero_telefonico % 1000 == 909:
        print("CONTESTAR")
    elif hora_llamada >= 17 and hora_llamada <= 19 and str(numero_telefonico)[0:3] != "877":
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")

numero = int(input("Ingrese el número telefónico (8 cifras): "))
hora = int(input("Ingrese la hora de la llamada (0-23): "))

contestar_celular(numero, hora)
