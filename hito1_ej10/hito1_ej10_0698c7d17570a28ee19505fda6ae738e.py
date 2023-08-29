#Cajero Automático
from time import sleep
cajero = 1000000
dinero_usuario = 100000
Usuario = str(int(input("Ingrese el usuario: ")))
contraseña = str(int(input("Ingrese la contraseña: ")))
while True:
    if Usuario == "10334151" and contraseña == "1803":
        print("Usuario y contraseña correctos")
        sleep(1)
        monto_a_retirar = int(input("Ingrese el monto a retirar: "))
        if monto_a_retirar>dinero_usuario and monto_a_retirar>cajero:
            print("monto no permitido")
            break
        if monto_a_retirar<dinero_usuario and monto_a_retirar<cajero:
            saldo_usuario_final = dinero_usuario-monto_a_retirar
            saldo_cajero_final = cajero-monto_a_retirar
            print("saldo cuenta=", saldo_usuario_final)
            print("saldo cajero=", saldo_cajero_final)
        if monto_a_retirar!="N":
            break
    if Usuario != "10334151" or contraseña != "1803":
        print("clave invalida")
        sleep(1)
        print("INTENTO N°2")
        sleep(1)
        contraseña = str(int(input("Ingrese la contraseña denuevo: ")))
        if Usuario != "10334151" or contraseña != "1803":
            print("clave invalida")
            sleep(1)
            print("INTENTO N°3")
            sleep(1)
            contraseña = str(int(input("Ingrese la contraseña denuevo: ")))
            if Usuario != "10334151" or contraseña != "1803":
                print("tarjeta bloqueada")
                break
           