#Cajero Automático
from time import sleep
saldo_cajero = 1000000
saldo_usuario = 100000
usu_ario = str(int(input("Ingresar usuario: ")))
contra_sena = str(int(input("Ingresar contraseña: ")))
while True:
    if usu_ario == "10334151" and contra_sena == "1803":
        print("El usuario y la contraseña estan correctos, se procede a")
        sleep(1)
        monto_a_retirar = int(input("Ingresar monto que va a retirar: "))
        if monto_a_retirar>saldo_usuario and monto_a_retirar>saldo_cajero:
            print("monto no permitido")
            break
        if monto_a_retirar<saldo_usuario and monto_a_retirar<saldo_cajero:
            saldo_usuario_final = saldo_usuario-monto_a_retirar
            saldo_cajero_final = saldo_cajero-monto_a_retirar
            print("saldo cuenta= ", saldo_usuario_final)
            print("saldo cajero= ", saldo_cajero_final)
            ##PLATA*
            p20k = int(monto_a_retirar/20000)
            monto_a_retirar = monto_a_retirar%20000
            p10k = int(monto_a_retirar/10000)
            monto_a_retirar = monto_a_retirar%10000
            p5k = int(monto_a_retirar/5000)
            monto_a_retirar = monto_a_retirar%5000
            ##PLATITA
            print("billetes 20000= ", p20k)
            print("billetes 10000= ", p10k)
            print("billetes 5000= ", p5k)
        if monto_a_retirar!="N":
            break     