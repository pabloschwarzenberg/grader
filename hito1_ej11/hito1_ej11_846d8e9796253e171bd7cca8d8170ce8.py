saldo_inicial = 1000000
saldo_cajero = 1000000
intentos = 0

billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        saldo_usuario = 100000
        break
    else:
        print("Usuario o clave incorrectos.")
        intentos += 1
        if intentos == 3:
            print("Tarjeta bloqueada.")
            exit()
while True:
    monto_retiro = int(input("Ingrese el monto a retirar: "))
    if monto_retiro <= 0 or monto_retiro > saldo_usuario:
        print("Monto no permitido.")
    else:
        billetes_20000_retiro = min(monto_retiro // 20000, billetes_20000)
        monto_retiro -= billetes_20000_retiro * 20000
        billetes_10000_retiro = min(monto_retiro // 10000, billetes_10000)
        monto_retiro -= billetes_10000_retiro * 10000
        billetes_5000_retiro = min(monto_retiro // 5000, billetes_5000)
        monto_retiro -= billetes_5000_retiro * 5000
        saldo_usuario -= (billetes_20000_retiro * 20000) + (billetes_10000_retiro * 10000) + (billetes_5000_retiro * 5000)
        saldo_cajero -= (billetes_20000_retiro * 20000) + (billetes_10000_retiro * 10000) + (billetes_5000_retiro * 5000)
        print("Billetes 20000 =", billetes_20000_retiro)
        print("Billetes 10000 =", billetes_10000_retiro)
        print("Billetes 5000 =", billetes_5000_retiro)

        print("Saldo cuenta =", saldo_usuario)
        print("Saldo cajero =", saldo_cajero)

    opcion = input("¿Desea realizar otro retiro? (S/N): ")
    if opcion.upper() != "S":
        break
