#Cajero Automático
saldo_inicial_cajero = {
    20000: 20,
    10000: 40,
    5000: 40
}

saldo_inicial_cuenta = 100000
intentos_fallidos = 0
saldo_cuenta = saldo_inicial_cuenta
saldo_cajero = saldo_inicial_cajero.copy()

usuario_valido = 10334151
clave_valida = 1803

while True:
    usuario = int(input("Ingrese su usuario: "))
    clave = int(input("Ingrese su clave: "))

    if usuario != usuario_valido or clave != clave_valida:
        intentos_fallidos += 1
        print("Clave inválida.")

        if intentos_fallidos == 3:
            print("Tarjeta bloqueada.")
            break
    else:
        intentos_fallidos = 0
        monto = float(input("Ingrese el monto a retirar: "))

        if monto > saldo_cuenta:
            print("Monto no permitido.")
        else:
            saldo_cuenta -= monto
            billetes_entregados = {}

            for valor_billete, cantidad_disponible in saldo_cajero.items():
                cantidad_billetes = min(int(monto / valor_billete), cantidad_disponible)
                monto -= valor_billete * cantidad_billetes
                saldo_cajero[valor_billete] -= cantidad_billetes
                billetes_entregados[valor_billete] = cantidad_billetes

            print(f"Saldo cuenta: {saldo_cuenta}")
            print(f"Saldo cajero: {saldo_cajero}")
            print("Billetes entregados:")
            for valor_billete, cantidad_billetes in billetes_entregados.items():
                print(f"Billetes {valor_billete}: {cantidad_billetes}")

    continuar = input("¿Desea realizar otra transacción? (S/N): ")
    if continuar.upper() == "N":
        break
      