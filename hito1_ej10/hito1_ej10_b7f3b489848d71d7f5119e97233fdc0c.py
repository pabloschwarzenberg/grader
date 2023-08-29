#Cajero Automático
from time import sleep
saldo_cajerooo = 1000000
saldo_usuario = 100000
usuarios = str(int(input("Ingrese el usuario: ")))
contrasenaa = str(int(input("Ingrese la contraseña: ")))
while True:
    if usuarios == "10334151" and contrasenaa == "1803":
        print("Usuario y contraseña correctos")
        sleep(1)
        monto_a_retirar = int(input("Ingrese el monto a retirar: "))
        if monto_a_retirar>saldo_usuario and monto_a_retirar>saldo_cajerooo:
            print("monto no permitido")
            break
        if monto_a_retirar<saldo_usuario and monto_a_retirar<saldo_cajerooo:
            saldo_usuario_final = saldo_usuario-monto_a_retirar
            saldo_cajerooo_final = saldo_cajerooo-monto_a_retirar
            print("saldo cuenta=", saldo_usuario_final)
            print("saldo cajero=", saldo_cajerooo_final)
        if monto_a_retirar!="N":
            break
    if usuarios != "10334151" or contrasenaa != "1803":
        print("clave invalida")
        sleep(1)
        print("INTENTO N°2")
        sleep(1)
        contrasenaa = str(int(input("Ingrese la contraseña denuevo: ")))
        if usuarios != "10334151" or contrasenaa != "1803":
            print("clave invalida")
            sleep(1)
            print("INTENTO N°3")
            sleep(1)
            contrasenaa = str(int(input("Ingrese la contraseña denuevo: ")))
            if usuario != "10334151" or contrasenaa != "1803":
                print("tarjeta bloqueada")
                break     