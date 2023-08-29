#Cajero Automático
from time import sleep
saldo = 1000000
saldo_usuario = 100000
usuario = str(int(input("Ingrese el usuario: ")))
password = str(int(input("Ingrese la contraseña: ")))
while True:
    if usuario == "10334151" and password == "1803":
        print("Usuario y contraseña correctos")
        sleep(1)
        retirar = int(input("Ingrese el monto a retirar: "))
        if retirar>saldo_usuario and retirar>saldo:
            print("monto no permitido")
            break
        if retirar<saldo_usuario and retirar<saldo:
            saldo_usuario_final = saldo_usuario - retirar
            saldo_cajero_final = saldo - retirar
            print("saldo cuenta=", saldo_usuario_final)
            print("saldo cajero=", saldo_cajero_final)
        if retirar!= "N":
            break
    if usuario != "10334151" or password != "1803":
        print("clave invalida")
        sleep(1)
        print("INTENTO N°2")
        sleep(1)
        password = str(int(input("Ingrese nuevamente: ")))
        if usuario != "10334151" or password != "1803":
            print("clave invalida")
            sleep(1)
            print("INTENTO N°3")
            sleep(1)
            password = str(int(input("Ingrese nuevamente: ")))
            if usuario != "10334151" or password != "1803":
                print("tarjeta bloqueada")
                break