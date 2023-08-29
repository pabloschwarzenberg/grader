#Cajero Automático
saldo_cajero = 1000000
saldo_cuenta = 100000
usuario = str(int(input("Ingrese el usuario: ")))
clave = str(int(input("Ingrese la contraseña: ")))

while True:
    if ((usuario == "10334151") and (clave == "1803")):
        print("Usuario y contraseña correctos")

    monto_retirar = int(input("Ingrese monto a retirar: "))
    if ((monto_retirar > saldo_cuenta) and (monto_retirar > saldo_cajero)):
        print("Monto no permitido")
        break
    if ((monto_retirar < saldo_cuenta) and (monto_retirar < saldo_cajero)):
        saldo_cuenta_final = saldo_cuenta - monto_retirar
        saldo_cajero_final = saldo_cajero - monto_retirar
        print("Saldo cuenta = ",saldo_cuenta_final)
        print("Saldo cajero = ",saldo_cajero_final)

        #billetes
        billete_20k = int(monto_retirar /20000)
        monto_retirar = monto_retirar %20000
        billete_10k = int(monto_retirar / 10000)
        monto_retirar = monto_retirar %10000
        billete_5k = int(monto_retirar / 5000)
        monto_retirar = monto_retirar %5000
        print("Billetes 20000 = ",billete_20k)
        print("Billetes 10000 = ",billete_10k)
        print("Billetes 5000 = ", billete_5k)
    if monto_retirar != "N":
        break

    if ((usuario != "10334151") or (clave != "1803")):
        print("Clave invalida")
        print("Intento N°2")
        clave = str(int(input("Ingrese la contraseña denuevo: ")))
        print("Clave invalida")
        print("Intento N°3")
        clave = str(int(input("Ingrese la contraseña denuevo: ")))
        if usuario != "10334151" or clave != "1803":
            print("tarjeta bloqueada")
            break



