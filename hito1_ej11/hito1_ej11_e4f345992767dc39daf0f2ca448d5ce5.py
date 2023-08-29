#Cajero Automático
from time import sleep
sc = 1000000
su = 100000
u = str(int(input("Ingrese el usuario: ")))
c = str(int(input("Ingrese la clave: ")))
while True:
    if u == "10334151" and c == "1803":
        print("Usuario y clave correctos")
        sleep(1)
        monto_a_retirar = int(input("Ingrese el monto a retirar: "))
        if monto_a_retirar>su and monto_a_retirar>sc:
            print("monto no permitido")
            break
        if monto_a_retirar<su and monto_a_retirar<sc:
            su_final = su-monto_a_retirar
            sc_final = sc-monto_a_retirar
            print("saldo cuenta=", su_final)
            print("saldo cajero=", sc_final)
            ##Billetes*
            b20k = int(monto_a_retirar/20000)
            monto_a_retirar = monto_a_retirar%20000
            b10k = int(monto_a_retirar/10000)
            monto_a_retirar = monto_a_retirar%10000
            b5k = int(monto_a_retirar/5000)
            monto_a_retirar = monto_a_retirar%5000
            ##Billetes
            print("billetes 20000= ", b20k)
            print("billetes 10000= ", b10k)
            print("billetes 5000= ", b5k)
        if monto_a_retirar!="N":
            break

    if u != "10334151" or c != "1803":
        print("clave invalida")
        sleep(1)
        print("INTENTO N°2")
        sleep(1)
        c = str(int(input("Ingrese la clave nuevamente: ")))
        if u != "10334151" or c != "1803":
            print("clave invalida")
            sleep(1)
            print("INTENTO N°3")
            sleep(1)
            c = str(int(input("Ingrese la clave denuevo: ")))
            if u != "10334151" or c != "1803":
                print("tarjeta bloqueada")
                break      