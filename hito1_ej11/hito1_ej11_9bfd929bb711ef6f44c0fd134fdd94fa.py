#Cajero Automático
cajero = 1000000
saldo_usuario = 100000
usuario = str(int(input("Ingrese el usuario: ")))
password = str(int(input("Ingrese la contraseña: ")))
while True:
    if usuario == "10334151" and password == "1803":
        print("Usuario y contraseña correctos")
        retiro = int(input("Ingrese el monto a retirar: "))

        if retiro>saldo_usuario and retiro>cajero:
            print("monto no permitido")
            break

        if retiro<saldo_usuario and retiro<cajero:
            saldo_usuario_final = saldo_usuario - retiro
            saldo_cajero_final = cajero - retiro
            print("saldo cuenta=", saldo_usuario_final)
            print("saldo cajero=", saldo_cajero_final)

            ##Billetes*
            b20k = int(retiro / 20000)
            retiro = retiro % 20000
            b10k = int(retiro / 10000)
            retiro = retiro % 10000
            b5k = int(retiro / 5000)
            retiro = retiro % 5000

            ##Billetes
            print("billetes 20000= ", b20k)
            print("billetes 10000= ", b10k)
            print("billetes 5000= ", b5k)

        if retiro != "N":
            break