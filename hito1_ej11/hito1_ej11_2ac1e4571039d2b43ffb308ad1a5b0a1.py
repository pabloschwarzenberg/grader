#Cajero Automático
from time import sleep
saldocajero = 1000000
saldousuario = 100000
user = str(int(input("Ingrese el usuario: ")))
contra = str(int(input("Ingrese la contraseña: ")))
while True:
    if user == "10334151" and contra == "1803":
        print("Usuario y contraseña correctos")
        sleep(1)
        montoretirar = int(input("Ingrese el monto a retirar: "))
        if montoretirar>saldousuario and montoretirar>saldocajero:
            print("monto no permitido")
            break
        if montoretirar<saldousuario and montoretirar<saldocajero:
            saldofinal_user = saldousuario-montoretirar
            saldocajerfinal = saldocajero-montoretirar
            print("saldo cuenta=", saldofinal_user)
            print("saldo cajero=", saldocajerfinal)
            ##Billetes*
            b20000 = int(montoretirar/20000)
            montoretirar = montoretirar%20000
            b10000 = int(montoretirar/10000)
            montoretirar = montoretirar%10000
            b5000 = int(montoretirar/5000)
            montoretirar = montoretirar%5000
            ##Billetes
            print("billetes 20000= ", b20000)
            print("billetes 10000= ", b10000)
            print("billetes 5000= ", b5000)
        if montoretirar!="N":
            break