#Cajero Automático
saldo_cuenta = 100000
saldo_cajero = {
    20000: 20,
    10000: 40,
    5000: 40
}

intentos_fallidos = 0

while True:
    usuario = "10334151"
    clave = "1803"

    if usuario == "10334151" and clave == "1803":
        print("Bienvenido, usuario 10334151")
        break
    else:
        print("Usuario o clave incorrectos.")
        intentos_fallidos += 1

        if intentos_fallidos >= 3:
            print("Tarjeta bloqueada. Programa finalizado.")
            exit()

while True:
    monto = int(input("Ingrese el monto a retirar: "))

    if monto > saldo_cuenta:
        print("Monto no permitido. Fondos insuficientes en la cuenta.")
    elif monto > sum(k * v for k, v in saldo_cajero.items()):
        print("Monto no permitido. Fondos insuficientes en el cajero.")
    else:
        saldo_cuenta -= monto
        billetes_entregados = {}

        for billete, cantidad in sorted(saldo_cajero.items(), reverse=True):
            if monto >= billete:
                cant_billetes = min(monto // billete, cantidad)
                monto -= cant_billetes * billete
                saldo_cajero[billete] -= cant_billetes
                billetes_entregados[billete] = cant_billetes

        print("Retiro exitoso.")
        print("Saldo cuenta =", saldo_cuenta)
        print("Saldo cajero =", saldo_cajero)
        print("Billetes entregados:")
        for billete, cantidad in billetes_entregados.items():
            print("Billetes", billete, "=", cantidad)

    opcion = input("¿Desea realizar otro retiro? (N para salir): ")
    if opcion.upper() == "N":
        break
     