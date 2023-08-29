#Contestador de celular
from time import sleep
numero = int(input("Ingrese nuemero telefónico: "))
hora = int(input("Ingrese hora de la llamada: "))

while True:
    if hora >= 0 and hora <= 7:
        print("CONTESTAR")
        sleep(1)
    if hora < 14:
        if numero % 1000 == 909:
            print("CONTESTAR")
            sleep(1)
            break
    if hora >= 17 and hora <= 19:
        if numero//1000==877:
            print("CONTESTAR")
            sleep(1)
            break
    if hora > 19:
        print("NO CONTESTAR")
        break
    else:
        print("NO CONTESTAR")
        sleep(1)
        break