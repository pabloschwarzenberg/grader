#Cajero Automático
saldo_cuenta = 100000
saldo_cajero = {
    20000: 20,
    10000: 40,
    5000: 40
}
intentos_fallidos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Inicio de sesión exitoso")
        break
    else:
        intentos_fallidos += 1
        print("Clave inválida")

    if intentos_fallidos == 3:
        print("Tarjeta bloqueada")
        exit()

while True:
    monto_retiro = int(input("Ingrese el monto a retirar: "))

    if monto_retiro > saldo_cuenta or monto_retiro <= 0:
        print("Monto no permitido")
    else:
        billetes_retiro = {}

        for denominacion, cantidad_disponible in saldo_cajero.items():
            cantidad_billetes = min(monto_retiro // denominacion, cantidad_disponible)
            billetes_retiro[denominacion] = cantidad_billetes
            monto_retiro -= denominacion * cantidad_billetes

        if monto_retiro == 0:
            for denominacion, cantidad_billetes in billetes_retiro.items():
                saldo_cajero[denominacion] -= cantidad_billetes
                print("Billetes", denominacion, "=", cantidad_billetes)

            saldo_cuenta -= monto_retiro
            saldo_cajero_total = sum(denominacion * cantidad for denominacion, cantidad in saldo_cajero.items())

            print("Retiro exitoso")
            print("Saldo cuenta =", saldo_cuenta)
            print("Saldo cajero =", saldo_cajero_total)
        else:
            print("No hay suficientes billetes para el monto solicitado")

    opcion = input("¿Desea realizar otro retiro? (S/N): ")
    if opcion.upper() != "S":
        break      