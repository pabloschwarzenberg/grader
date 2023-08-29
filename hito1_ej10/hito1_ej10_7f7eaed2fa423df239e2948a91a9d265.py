#Cajero Automático
from time import sleep
saldo_cajero = 1000000
saldo_cuenta = 100000
usuario = str(int(input("Ingrese el usuario: ")))
clave = str(int(input("Ingrese la contraseña: ")))
while True:
    if usuario == "10334151" and clave == "1803":
        print("Usuario y contraseña correctos")
        sleep(1)
        monto_a_retirar = int(input("Ingrese el monto a retirar: "))
        if monto_a_retirar>saldo_cuenta and monto_a_retirar>saldo_cajero:
            print("monto no permitido")
            break
        if monto_a_retirar<saldo_cuenta and monto_a_retirar<saldo_cajero:
            saldo_cuenta_total = saldo_cuenta-monto_a_retirar
            saldo_cajero_total = saldo_cajero-monto_a_retirar
            print("saldo cuenta=", saldo_cuenta_total)
            print("saldo cajero=", saldo_cajero_total)
        if monto_a_retirar!="N":
            break
    if usuario != "10334151" or clave != "1803":
        print("clave invalida")
        sleep(1)
        print("INTENTO N°2")
        sleep(1)
        clave = str(int(input("Ingrese la contraseña nuevamente: ")))
        if usuario != "10334151" or clave != "1803":
            print("clave invalida")
            sleep(1)
            print("INTENTO N°3")
            sleep(1)
            clave = str(int(input("Ingrese la contraseña nuevamente: ")))
            if usuario != "10334151" or clave != "1803":
                print("tarjeta bloqueada")
                break
