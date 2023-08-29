#Cajero Automático
saldo_cuenta = 1000000
saldo_cajero = {
    20000: 20,
    10000: 40,
    5000: 40
}

def imprimir_billetes(billetes):
    for billete, cantidad in billetes.items():
        print(f"Billetes {billete}: {cantidad}")

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Inicio de sesión exitoso.")
        intentos_fallidos = 0

        while True:
            monto = int(input("Ingrese el monto a retirar: "))

            if monto <= saldo_cuenta:
                monto_disponible = monto
                billetes_entregados = {}

                for billete, cantidad in saldo_cajero.items():
                    if monto_disponible >= billete and cantidad > 0:
                        cant_billetes = min(int(monto_disponible / billete), cantidad)
                        monto_disponible -= billete * cant_billetes
                        saldo_cajero[billete] -= cant_billetes
                        billetes_entregados[billete] = cant_billetes

                if monto_disponible == 0:
                    saldo_cuenta -= monto
                    print("Retiro exitoso.")
                    print(f"Saldo cuenta: {saldo_cuenta}")
                    print(f"Saldo cajero: {saldo_cajero}")
                    imprimir_billetes(billetes_entregados)
                else:
                    print("Monto no permitido. El cajero no tiene los billetes necesarios.")
            else:
                print("Monto no permitido. El saldo de la cuenta no es suficiente.")

            continuar = input("¿Desea realizar otro retiro? (S/N): ")
            if continuar.upper() != "S":
                break
    else:
        intentos_fallidos += 1
        print("Clave inválida.")

        if intentos_fallidos == 3:
            print("Tarjeta bloqueada.")
            break
      