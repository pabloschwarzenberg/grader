#Cajero Automático
from time import sleep
saldo_cajero = 1000000
saldo_usuario = 100000
usuario = str(int(input("Ingrese el usuario: ")))
contrasena = str(int(input("Ingrese la contraseña: ")))
while True:
    if usuario == "10334151" and contrasena == "1803":
        print("Usuario y contraseña correctos")
        sleep(1)
        monto_retirar = int(input("Ingrese el monto a retirar: "))
        if monto_retirar>saldo_usuario and monto_retirar>saldo_cajero:
            print("monto no permitido")
            break
        if monto_retirar<saldo_usuario and monto_retirar<saldo_cajero:
            saldo_usuario_final = saldo_usuario-monto_retirar
            saldo_cajero_final = saldo_cajero-monto_retirar
            print("saldo cuenta=", saldo_usuario_final)
            print("saldo cajero=", saldo_cajero_final)
            ##Billetes*
            b20k = int(monto_retirar/20000)
            monto_retirar = monto_retirar%20000
            b10k = int(monto_retirar/10000)
            monto_retirar = monto_retirar%10000
            b5k = int(monto_retirar/5000)
            monto_retirar = monto_retirar%5000
            ##Billetes
            print("billetes 20000= ", b20k)
            print("billetes 10000= ", b10k)
            print("billetes 5000= ", b5k)
        if monto_retirar!="N":
            break
  
    if usuario != "10334151" or contrasena != "1803":
        print("clave invalida")
        sleep(1)
        print("INTENTO N°2")
        sleep(1)
        contrasena = str(int(input("Ingrese la contraseña denuevo: ")))
        if usuario != "10334151" or contrasena != "1803":
            print("clave invalida")
            sleep(1)
            print("INTENTO N°3")
            sleep(1)
            contrasena = str(int(input("Ingrese la contraseña denuevo: ")))
            if usuario != "10334151" or contrasena != "1803":
                print("tarjeta bloqueada")
                break