saldo_cuenta = 1000000
billetes = {
    20000: 20,
    10000: 40,
    5000: 40
}

usuario = int(input("Ingrese su usuario: "))
clave = int(input("Ingrese su clave: "))

if usuario == 10334151 and clave == 1803:
    intentos_fallidos = 0
    saldo_usuario = 100000

    while True:
        monto_retiro = int(input("Ingrese el monto a retirar: "))

        if monto_retiro > saldo_usuario:
            print("Monto no disponible en su cuenta.")
        elif monto_retiro > saldo_cuenta:
            print("Monto no disponible en el cajero.")
        else:
            billetes_retiro = {}
            saldo_cuenta -= monto_retiro
            saldo_usuario -= monto_retiro

            for valor, cantidad in billetes.items():
                if monto_retiro >= valor:
                    cantidad_retiro = min(monto_retiro // valor, cantidad)
                    billetes_retiro[valor] = cantidad_retiro
                    monto_retiro -= valor * cantidad_retiro
                    billetes[valor] -= cantidad_retiro

            print("Retiro exitoso.")
            print("Saldo cuenta=", saldo_usuario)
            print("Saldo cajero=", saldo_cuenta)
            for valor, cantidad in billetes_retiro.items():
                print("billetes", valor, "=", cantidad)

        opcion_salida = input("¿Desea realizar otra transacción? (S/N): ")
        if opcion_salida.upper() != "S":
            break
else:
    print("Usuario o clave incorrectos.")

