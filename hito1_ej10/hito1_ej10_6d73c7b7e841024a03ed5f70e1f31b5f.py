#Cajero Automático
from time import sleep
saldo_cajero = 1000000
saldo_usuario = 100000
usuario = str(int(input("Ingrese el usuario: ")))
contrasena = str(int(input("Ingrese la contraseña: ")))
while True:
    if usuario == "10334151" and contrasena == "1803":
        print("Usuario y contraseña validos")
        sleep(1)
        monto_a_retirar = int(input("Ingrese el monto que desea retirar: "))
        if monto_a_retirar>saldo_usuario and monto_a_retirar>saldo_cajero:
            print("monto no valido")
            break
        if monto_a_retirar<saldo_usuario and monto_a_retirar<saldo_cajero:
            saldo_usuario_final = saldo_usuario-monto_a_retirar
            saldo_cajero_final = saldo_cajero-monto_a_retirar
            print("saldo cuenta=", saldo_usuario_final)
            print("saldo cajero=", saldo_cajero_final)
        if monto_a_retirar!="N":
            break
    if usuario != "10334151" or contrasena != "1803":
        print("clave incorrecta")
        sleep(1)
        print("INTENTO 2")
        sleep(1)
        contrasena = str(int(input("Ingrese de nuevo su contraseña: ")))
        if usuario != "10334151" or contrasena != "1803":
            print("clave incorrecta")
            sleep(1)
            print("INTENTO 3")
            sleep(1)
            contrasena = str(int(input("Ingrese la contraseña denuevo: ")))
            if usuario != "10334151" or contrasena != "1803":
                print("tarjeta bloqueada")
                break      