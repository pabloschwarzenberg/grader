#Cajero Automático
from time import sleep
dinero_cajero = 1000000
dinero_usuario = 100000
usua_rio = str(int(input("Inserte su usuario: ")))
cla_ve = str(int(input("Ingrese su contraseña: ")))
while True:
    if usua_rio == "10334151" and cla_ve == "1803":
        print("Usuario y Contraseña correctos, se pasa a...")
        sleep(1)
        monto_a_retirar = int(input("Ingresar monto que va a retirar: "))
        if monto_a_retirar>dinero_usuario and monto_a_retirar>dinero_cajero:
            print("Monto NO permitido")
            break
        if monto_a_retirar<dinero_usuario and monto_a_retirar<dinero_cajero:
            dinero_usuario_final = dinero_usuario-monto_a_retirar
            dinero_cajero_final = dinero_cajero-monto_a_retirar
            print("saldo cuenta= ", dinero_usuario_final)
            print("saldo cajero= ", dinero_cajero_final)
            #
            p20k = int(monto_a_retirar/20000)
            monto_a_retirar = monto_a_retirar%20000
            p10k = int(monto_a_retirar/10000)
            monto_a_retirar = monto_a_retirar%10000
            p5k = int(monto_a_retirar/5000)
            monto_a_retirar = monto_a_retirar%5000
            #
            print("billetes 20000= ", p20k)
            print("billetes 10000= ", p10k)
            print("billetes 5000= ", p5k)
        if monto_a_retirar!="N":
            break        