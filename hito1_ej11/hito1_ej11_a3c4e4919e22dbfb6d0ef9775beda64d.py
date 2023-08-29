from time import sleep
sCajero = 1000000
sUsuario = 100000
user = str(int(input("Ingrese el usuario: ")))
password = str(int(input("Ingrese la contraseña: ")))
while True:
    if user == "10334151" and password == "1803":
        print("usuario y contraseña CORRECTOS")
        sleep(1)
        mRetirar = int(input("Ingrese el monto a retirar: "))
        if mRetirar > sUsuario and mRetirar > sCajero:
            print("MONTO NO PERMITIDO")
            break
        if mRetirar  < sUsuario and mRetirar < sCajero:
            sUsuario_final = sUsuario - mRetirar
            sCajero_final = sCajero - mRetirar
            print("saldo cuenta=", sUsuario_final)
            print("saldo cajero=", sCajero_final)
            ##Billetes*
            b20k = int(mRetirar/20000)
            mRetirar = mRetirar % 20000
            b10k = int(mRetirar/10000)
            mRetirar = mRetirar%10000
            b5k = int(mRetirar/5000)
            mRetirar = mRetirar%5000
            ##Billetes
            print("billetes 20000= ", b20k)
            print("billetes 10000= ", b10k)
            print("billetes 5000= ", b5k)
        if mRetirar != "N":
            break
  
    if user != "10334151" or password != "1803":
        print("CLAVE INVALIDA")
        sleep(1)
        print("INTENTO N°2")
        sleep(1)
        password = str(int(input("Ingrese la contraseña nuevamente: ")))
        if user != "10334151" or password != "1803":
            print("CLAVE INVALIDA")
            sleep(1)
            print("INTENTO N°3")
            sleep(1)
            password = str(int(input("Ingrese la contraseña nuevamente: ")))
            if user != "10334151" or password != "1803":
                print("TARJETA BLOQUEADA")
                break

