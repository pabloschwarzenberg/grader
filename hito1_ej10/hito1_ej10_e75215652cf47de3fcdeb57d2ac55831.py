#Cajero Automático
from time import sleep
sc= 1000000
su= 100000
u= str(int(input("Ingrese el usuario: ")))
c= str(int(input("Ingrese la contraseña: ")))
while True:
    if u== "10334151" and c== "1803":
        print("Usuario y contraseña correctos")
        sleep(1)
        mr= int(input("Ingrese el monto a retirar: "))
        if mr>su and mr>sc:
            print("Monto no permitido")
            break
        if mr<su and mr<sc:
            suf = su-mr
            scf= sc-mr
            print("Saldo Cuenta=", suf)
            print("Saldo Cajero=", scf)
        if mr !="N":
            break
    if u != "10334151" or c != "1803":
        print("Clave invalida")
        sleep(1)
        print("Intento N°2")
        sleep(1)
        c= str(int(input("Ingrese la contraseña denuevo: ")))
        if u != "10334151" or c != "1803":
            print("Clave invalida")
            sleep(1)
            print("Intento N°3")
            sleep(1)
            c= str(int(input("Ingrese la contraseña denuevo: ")))
            if u != "10334151" or c != "1803":
                print("Tarjeta bloqueada")
                break