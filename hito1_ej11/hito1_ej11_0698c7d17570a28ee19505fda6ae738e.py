from time import sleep
S_cajero = 1000000
S_Usuario = 100000
usuario = str(int(input("Ingrese el usuario: ")))
contraseña = str(int(input("Ingrese la contraseña: ")))
while True:
    if usuario == "10334151" and contraseña == "1803":
        print("Usuario y contraseña correctos")
        sleep(1)
        monto_a_retirar = int(input("Ingrese el monto a retirar: "))
        if monto_a_retirar>S_Usuario and monto_a_retirar>S_cajero:
            print("monto no permitido")
            break
        if monto_a_retirar<S_Usuario and monto_a_retirar<S_cajero:
            saldo_usuario_final = S_Usuario-monto_a_retirar
            saldo_cajero_final = S_cajero-monto_a_retirar
            print("saldo cuenta=", saldo_usuario_final)
            print("saldo cajero=", saldo_cajero_final)
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
  
    if usuario != "10334151" or contraseña != "1803":
        print("clave invalida")
        sleep(1)
        print("INTENTO N°2")
        sleep(1)
        contraseña = str(int(input("Ingrese la contraseña denuevo: ")))
        if usuario != "10334151" or contraseña != "1803":
            print("clave invalida")
            sleep(1)
            print("INTENTO N°3")
            sleep(1)
            contraseña = str(int(input("Ingrese la contraseña denuevo: ")))
            if usuario != "10334151" or contraseña != "1803":
                print("tarjeta bloqueada")
                break    