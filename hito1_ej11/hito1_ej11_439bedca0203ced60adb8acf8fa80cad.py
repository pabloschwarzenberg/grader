from time import sleep

saldo_cajero = 1000000
saldo_usuario = 100000

usuario = str(int(input("Ingrese el usuario: ")))
contraseña = str(int(input("Ingrese la contraseña: ")))

while True:
    if usuario == "10334151" and contraseña == "1803":
        print("Usuario y contraseña correctos")
        sleep(1)
        monto_a_retirar = int(input("Ingrese el monto a retirar: "))

        if monto_a_retirar > saldo_usuario and monto_a_retirar > saldo_cajero:
            print("Monto no permitido")
            break

        if monto_a_retirar < saldo_usuario and monto_a_retirar < saldo_cajero:
            saldo_usuario_final = saldo_usuario - monto_a_retirar
            saldo_cajero_final = saldo_cajero - monto_a_retirar
            print("Saldo cuenta =", saldo_usuario_final)
            print("Saldo cajero =", saldo_cajero_final)

            # Billetes
            b20k = int(monto_a_retirar / 20000)
            monto_a_retirar = monto_a_retirar%20000
            b10k = int(monto_a_retirar / 10000)
            monto_a_retirar=monto_a_retirar%10000
            b5k = int(monto_a_retirar / 5000)
            monto_a_retirar = monto_a_retirar%5000
            
            print("Billetes 20000= ", b20k)
            print("Billetes 10000= ", b10k)
            print("Billetes 5000= ", b5k)
        if monto_a_retirar!="N":
            break
    if usuario!= "10334151" and contraseña!= "1803":
        print("clave invalida")
        sleep(1)
        print("INTENTO N°2")
        sleep(1)
        contraseña = str(int(input("Ingrese la contraseña: ")))
        if usuario == "10334151" and contraseña == "1803":
            print("clave invalida")
            sleep(1)
            print("INTENTO N°3")
            sleep(1)
            contraseña = str(int(input("Ingrese la contraseña denuevo: ")))
            if usuario == "10334151" and contraseña == "1803":
                print("tarjeta bloqueada")
                break
