import random

def cajero_automatico():
    saldo_cuenta = 1000000
    billetes_disponibles = {
        20000: 20,
        10000: 40,
        5000: 40
    }

    while True:
        usuario = input("Ingrese su usuario: ")
        clave = input("Ingrese su clave: ")

        if usuario == "10334151" and clave == "1803":
            monto_retiro = int(input("Ingrese el monto a retirar: "))

            if monto_retiro <= saldo_cuenta:
                # Verificar disponibilidad de billetes
                billetes_entregados = {}
                for denominacion, cantidad in billetes_disponibles.items():
                    cant_billetes = min(cantidad, monto_retiro // denominacion)
                    monto_retiro -= cant_billetes * denominacion
                    billetes_entregados[denominacion] = cant_billetes

                if monto_retiro == 0:
                    # Actualizar saldos y billetes disponibles
                    saldo_cuenta -= sum(billetes_entregados.values()) * list(billetes_entregados.keys())[0]
                    for denominacion, cantidad in billetes_entregados.items():
                        billetes_disponibles[denominacion] -= cantidad

                    # Imprimir los billetes entregados
                    print("Retiro exitoso. Billetes entregados:")
                    for denominacion, cantidad in billetes_entregados.items():
                        print(f"billetes {denominacion}={cantidad}")

                    # Imprimir saldos actualizados
                    print("Saldo actual:")
                    print(f"Saldo cuenta: {saldo_cuenta}")
                    print("Saldos billetes disponibles:")
                    for denominacion, cantidad in billetes_disponibles.items():
                        print(f"billetes {denominacion}={cantidad}")
                else:
                    print("No se puede retirar el monto solicitado. Monto no permitido.")
            else:
                print("No se puede retirar el monto solicitado. Saldo insuficiente en la cuenta.")
        else:
            print("Clave inválida.")

        respuesta = input("¿Desea realizar otra transacción? (S/N): ")
        if respuesta.upper() != "S":
            break

    print("Gracias por utilizar el cajero automático.")

cajero_automatico()
