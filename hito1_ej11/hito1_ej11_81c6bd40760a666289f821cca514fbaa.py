#Cajero Automático
from time import sleep
saldo_caja = 1000000
saldo_user = 100000
user = str(int(input("Ingrese el usuario: ")))
passw = str(int(input("Ingrese la contraseña: ")))
while True:
    if user == "10334151" and passw == "1803":
        print("Usuario y contraseña correctos")
        sleep(1)
        monto_a_retirar = int(input("Ingrese el monto a retirar: "))
        if monto_a_retirar>saldo_user and monto_a_retirar>saldo_caja:
            print("Monto no permitido")
            break
        if monto_a_retirar<saldo_user and monto_a_retirar<saldo_caja:
            saldo_usuario_final = saldo_user-monto_a_retirar
            saldo_cajero_final = saldo_caja-monto_a_retirar
            print("Saldo cuenta=", saldo_usuario_final)
            print("Saldo cajero=", saldo_cajero_final)
            ##Billetes*
            b20k = int(monto_a_retirar/20000)
            monto_a_retirar = monto_a_retirar%20000
            b10k = int(monto_a_retirar/10000)
            monto_a_retirar = monto_a_retirar%10000
            b5k = int(monto_a_retirar/5000)
            monto_a_retirar = monto_a_retirar%5000
            ##Billetes
            print("Billetes 20000= ", b20k)
            print("Billetes 10000= ", b10k)
            print("Billetes 5000= ", b5k)
        if monto_a_retirar!="N":
            break      