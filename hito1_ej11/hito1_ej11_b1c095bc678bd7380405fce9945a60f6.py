#Cajero Automático
saldo_cajero = {
    20000: 20,
    10000: 40,
    5000: 40
}

saldo_cuenta = 100000
intentos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Inicio de sesión exitoso.")
        break
    else:
        intentos += 1
        print("Clave inválida.")

        if intentos == 3:
            print("Tarjeta bloqueada.")
            exit()

while True:
    monto = float(input("Ingrese el monto a retirar: "))

    if monto <= 0:
        print("Monto no permitido.")
    elif monto > saldo_cuenta:
        print("Saldo insuficiente.")
    elif monto > sum(billetes * cantidad for billetes, cantidad in saldo_cajero.items()):
        print("Cajero sin suficiente efectivo.")
    else:
        billetes_entregados = {}

        for billetes, cantidad in saldo_cajero.items():
            if monto >= billetes and cantidad > 0:
                cantidad_entregada = min(monto // billetes, cantidad)
                billetes_entregados[billetes] = cantidad_entregada
                monto -= billetes * cantidad_entregada
                saldo_cajero[billetes] -= cantidad_entregada

        saldo_cuenta -= monto

        print(f"Retiro exitoso. Saldo cuenta: {saldo_cuenta}. Saldo cajero: {saldo_cajero}")
        print("Billetes entregados:")
        for billetes, cantidad_entregada in billetes_entregados.items():
            print(f"billetes {billetes} = {cantidad_entregada}")

    continuar = input("¿Desea realizar otra transacción? (S/N): ")
    if continuar.upper() != "S":
        break
      