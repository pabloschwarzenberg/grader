def distribuir_billetes(monto):
    saldo = {
        20000: 20,
        10000: 40,
        5000: 40
    }

 
        monto -= cantidad_billetes * billete
        saldo[billete] -= cantidad_billetes
        billetes_entregados[billete] = cantidad_billetes

    return billetes_entregados


def main():
    saldo_inicial = {
        20000: 20,
        10000: 40,
        5000: 40
    }

    print("Bienvenido al cajero automático")
    print("Saldo inicial del cajero:")
    for billete, cantidad in saldo_inicial.items():
        print(f"{cantidad} billetes de {billete}")

    monto_retiro = int(input("Ingrese el monto que desea retirar: "))
    billetes_entregados = distribuir_billetes(monto_retiro)

    print("Billetes entregados:")
    for billete, cantidad in billetes_entregados.items():
        if cantidad > 0:
            print(f"{cantidad} billete(s) de {billete}")


if __name__ == "__main__":
    main()
