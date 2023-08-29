def validar_clave(usuario, clave):
    if usuario == "10334151" and clave == "1803":
        return True
    else:
        return False

saldo_cuenta = 100000
saldo_cajero = {
    20000: 20,
    10000: 40,
    5000: 40
}
intentos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if validar_clave(usuario, clave):
        intentos = 0
        monto = float(input("Ingrese el monto a retirar: "))

        if monto <= saldo_cuenta and monto <= sum(billetes * valor for valor, billetes in saldo_cajero.items()):
            billetes_retirados = {}

            for valor, cantidad in saldo_cajero.items():
                billetes_retirados[valor] = min(int(monto / valor), cantidad)
                monto -= valor * billetes_retirados[valor]
                saldo_cajero[valor] -= billetes_retirados[valor]

            print("Retiro exitoso.")
            print(f"Saldo cuenta: {saldo_cuenta}")
            print(f"Saldo cajero: {saldo_cajero}")
            print("Billetes retirados:")

            for valor, cantidad in billetes_retirados.items():
                print(f"Billetes {valor} = {cantidad}")

        else:
            print("Monto no permitido.")
    else:
        intentos += 1
        print("Clave inválida.")

    if intentos >= 3:
        print("Tarjeta bloqueada.")
        break

    opcion = input("¿Desea realizar otro retiro? (N para salir): ")
    if opcion.upper() == "N":
        break
