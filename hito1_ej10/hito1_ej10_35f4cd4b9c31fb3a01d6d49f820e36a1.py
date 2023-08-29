#Cajero Automático
from time import sleep
saldo_c = 1000000
saldo_us = 100000
us = str(int(input("usuario: ")))
contra = str(int(input("introduzca la contraseña: ")))
while True:
    if us == "10334151" and contra == "1803":
        print("Usuario y contraseña correctos")
        sleep(1)
        monto_retiro = int(input("Ingrese el monto a retirar: "))
        if monto_retiro>saldo_us and monto_retiro>saldo_c:
            print("monto no permitido")
            break
        if monto_retiro < saldo_us and monto_retiro < saldo_c:
           saldo_us_f = saldo_us - monto_retiro
           saldo_c_f = saldo_c - monto_retiro
           print("saldo de cuenta=", saldo_us_f)
           print("saldo del cajero=", saldo_c_f)
        if monto_retiro!="N":
           break
    if us != "10334151" or contra != "1803":
        print("clave incorrecta")
        sleep(1)
        print("intento 2")
        sleep(1)
        contra = str(int(input("Ingrese la contraseña otraves: ")))
        if us != "10334151" or contra != "1803":
            print("clave incorrecta")
            sleep(1)
            print("intento 3")
            sleep(1)
            contra = str(int(input("Ingrese la contraseña otraves: ")))
            if us != "10334151" or contra != "1803":
                print("tarjeta bloqueada")
                break 