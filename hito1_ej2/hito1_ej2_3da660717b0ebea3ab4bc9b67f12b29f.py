#Contestador de celular
from time import sleep
Numero_telefonico = int(input("Ingrese su número telefónico: "))
Hora_de_llamada = int(input("Ingrese su hora de llamada: "))
while True:
    if Hora_de_llamada >= 0 and Hora_de_llamada <=7:
        print("CONTESTAR")
        sleep(1)
        break
    if Hora_de_llamada < 14:
        if Numero_telefonico%1000 == 909:
            print("CONTESTAR")
            sleep (1)
            break
    if Hora_de_llamada >= 14 and Hora_de_llamada <= 19:
        if Numero_telefonico // 1000 == 877:
            print("CONTESTAR")
            sleep (1)
            break
    if Hora_de_llamada < 19:
        print("NO CONTESTAR")
        break
    else:
        print("NO CONTESTAR")
        sleep (1)
        break