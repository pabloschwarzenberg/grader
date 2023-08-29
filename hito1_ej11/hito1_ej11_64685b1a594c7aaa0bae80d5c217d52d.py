#Cajero Automático
from time import sleep
saldo_cajero = 1000000
saldo_usuario = 100000

usuario = str(int(input("Ingrese el usuario: ")))

contraseña = str(int(input("Ingrese la contraseña: ")))

while True:
    if usuario == "10334151" and contraseña == "1803":
        print("Su usuario y contraseña son correctos")
        sleep(1)
        monto_a_retirar = int(input("Ingrese el monto que desea retirar: "))

        if monto_a_retirar>saldo_usuario and monto_a_retirar>saldo_cajero:
            print("Monto no permitido")
            break

        if monto_a_retirar<saldo_usuario and monto_a_retirar<saldo_cajero:
            saldo_usuario_final = saldo_usuario-monto_a_retirar
            saldo_cajero_final = saldo_cajero-monto_a_retirar
            print("saldo cuenta=", saldo_usuario_final)
            print("saldo cajero=", saldo_cajero_final)
            
            b2 = int(monto_a_retirar/20000)
            monto_a_retirar = monto_a_retirar%20000
            b1 = int(monto_a_retirar/10000)
            monto_a_retirar = monto_a_retirar%10000
            b5 = int(monto_a_retirar/5000)
            monto_a_retirar = monto_a_retirar%5000
           
            print("billetes 20000= ", b2)
            print("billetes 10000= ", b1)
            print("billetes 5000= ", b5)

        if monto_a_retirar!="N":
            break      