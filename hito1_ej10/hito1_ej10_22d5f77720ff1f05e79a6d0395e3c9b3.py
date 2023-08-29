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
    if (monto_retirar != "N"):
        break

    if ((usuario != "10334151") or (clave !="1803")):
        print("Clave invalida")
        print("Intento N°2")
        clave = str(int(input("Ingrese la contraseña denuevo: ")))
        print("Clave invalida")
        print("Intento N°3")
        clave = str(int(input("Ingrese la contraseña denuevo: ")))
        if usuario != "10334151" or clave != "1803":
            print("tarjeta bloqueada")
            break



