saldo_cuenta = 100000
billetes = {
    20000: 20,
    10000: 40,
    5000: 40
}
intentos_fallidos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        while True:
            monto_retiro = float(input("Ingrese el monto a retirar: "))

            if monto_retiro <= saldo_cuenta:
                if monto_retiro <= sum(billetes[valor] * valor for valor in billetes):
                    billetes_retiro = {}

                    for valor in sorted(billetes.keys(), reverse=True):
                        cantidad_billetes = min(monto_retiro // valor, billetes[valor])
                        monto_retiro -= cantidad_billetes * valor
                        billetes[valor] -= cantidad_billetes
                        billetes_retiro[valor] = cantidad_billetes

                    saldo_cuenta -= monto_retiro

                    print("Retiro exitoso")
                    print("Saldo cuenta =", saldo_cuenta)
                    print("Saldo cajero =", sum(billetes[valor] * valor for valor in billetes))
                    print("Billetes entregados:")
                    for valor, cantidad in billetes_retiro.items():
                        print("billetes", valor, "=", cantidad)
                else:
                    print("Monto no permitido. Fondos insuficientes en el cajero.")
            else:
                print("Monto no permitido. Fondos insuficientes en la cuenta.")

            continuar = input("¿Desea realizar otro retiro? (S/N): ")
            if continuar.upper() != "S":
                break
        break

    else:
        intentos_fallidos += 1
        print("Clave inválida")

        if intentos_fallidos == 3:
            print("Tarjeta bloqueada")
            break

# FIN