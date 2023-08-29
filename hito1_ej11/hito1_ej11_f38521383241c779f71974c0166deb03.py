#Cajero Automático
from time import sleep
saldo_inicial_cajero = 1000000
saldo_inicial = 100000
usuario = str(int(input("Ingrese el usuario:")))

clave = str(int(input("Ingrese la contraseña:")))
while True:
    if clave == "1803" and usuario == "10334151":
        print("Usuario y Contraseña correctas")
        sleep(1)
        monto_a_retirar = int(input("Ingrese el monto a retirar:"))
        if monto_a_retirar > saldo_inicial and monto_a_retirar > saldo_inicial_cajero:
            print("monto no permitido")
            break
        if monto_a_retirar < saldo_inicial and monto_a_retirar < saldo_inicial_cajero:
            saldo_usuario_final = saldo_inicial-monto_a_retirar
            saldo_cajero_final = saldo_inicial_cajero-monto_a_retirar
            print("saldo cuenta=", saldo_usuario_final)
            print("saldo cajero=", saldo_cajero_final)
            b20k = int(monto_a_retirar/20000)
            monto_a_retirar = monto_a_retirar % 20000
            b10k = int(monto_a_retirar / 10000)
            monto_a_retirar = monto_a_retirar % 10000
            b5k = int(monto_a_retirar / 5000)
            monto_a_retirar = monto_a_retirar % 5000
            print("billetes 20000=", b20k)
            print("billetes 10000=", b10k)
            print("billetes 5000=", b5k)
        if monto_a_retirar != "N":
            break