saldo_cuenta = 100000
saldo_cajero = {20000: 20, 10000: 40, 5000: 40}
intentos_fallidos = 0

usuario_valido = 10334151
clave_valida = 1803

def imprimir_billetes(billetes):
    for denominacion, cantidad in billetes.items():
        print("billetes {}={}".format(denominacion, cantidad))

while True:
    usuario = int(input("Ingrese su número de usuario: "))
    clave = int(input("Ingrese su clave: "))

    if usuario != usuario_valido or clave != clave_valida:
        intentos_fallidos += 1
        print("Clave inválida.")

        if intentos_fallidos >= 3:
            print("Tarjeta bloqueada.")
            break
    else:
        monto_retiro = float(input("Ingrese el monto a retirar: "))

        if monto_retiro > saldo_cuenta or monto_retiro <= 0:
            print("Monto no permitido.")
        else:
            billetes_entregados = {}

            for denominacion, cantidad in sorted(saldo_cajero.items(), reverse=True):
                if monto_retiro >= denominacion and cantidad > 0:
                    cantidad_billetes = min(int(monto_retiro / denominacion), cantidad)
                    monto_retiro -= denominacion * cantidad_billetes
                    saldo_cajero[denominacion] -= cantidad_billetes
                    billetes_entregados[denominacion] = cantidad_billetes

            if monto_retiro > 0:
                print("Monto no permitido.")
            else:
                saldo_cuenta -= monto_retiro

                print("Saldo cuenta:", saldo_cuenta)
                print("Saldo cajero:", saldo_cajero)
                imprimir_billetes(billetes_entregados)

    opcion = input("¿Desea realizar otra transacción? (S/N): ")
    if opcion.upper() != "S":
        break