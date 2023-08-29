#Cajero Automático
saldo_cajero = 1000000
saldo_usuario = 100000
user = 10334151
passw = 1803

billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

intentos = 0

while True:
    usuario = int(input("Ingrese el usuario: "))
    clave = int(input("Ingrese su clave: "))

    if usuario == user and clave == passw:
        print("Acceso permitido.")
        break
    else:
        intentos += 1
        print("Clave inválida.")
        if intentos >= 3:
            print("Tarjeta bloqueada.")
            break

while True:
    monto = int(input("¿Cuánto desea retirar?: "))

    if monto > saldo_usuario or monto > saldo_cajero:
        print("Monto no permitido.")
    else:
        b20000 = min(monto // 20000, billetes_20000)
        monto -= b20000 * 20000

        b10000 = min(monto // 10000, billetes_10000)
        monto -= b10000 * 10000

        b5000 = min(monto // 5000, billetes_5000)
        monto -= b5000 * 5000

        if monto == 0:
            saldo_usuario -= (b20000 * 20000) + (b10000 * 10000) + (b5000 * 5000)
            saldo_cajero -= (b20000 * 20000) + (b10000 * 10000) + (b5000 * 5000)

            print("Saldo cuenta =", saldo_usuario)
            print("Saldo cajero =", saldo_cajero)

            print("Billetes entregados:")
            print("Billetes 20000 =", b20000)
            print("Billetes 10000 =", b10000)
            print("Billetes 5000 =", b5000)

            break
        else:
            print("No hay suficientes billetes para entregar el monto completo.")

    respuesta = input("¿Desea realizar otro retiro? (S/N): ")
    if respuesta.upper() != "S":
        break
