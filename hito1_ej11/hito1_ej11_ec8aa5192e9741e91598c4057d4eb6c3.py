saldo_inicial = 1000000
saldo_cajero = 1000000
intentos_fallidos = 0
usuario_valido = "10334151"
clave_valida = "1803"
saldo_usuario = 100000

billetes_disponibles = {
    20000: 20,
    10000: 40,
    5000: 40
}

while True:
    usuario = usuario_valido
    clave = clave_valida

    if usuario == usuario_valido and clave == clave_valida:
        print("Bienvenido/a,", usuario)

        monto_retiro = 45000  # Modifica este valor según tus necesidades

        if monto_retiro > saldo_usuario or monto_retiro <= 0:
            print("Monto no permitido")
        else:
            billetes_entregados = {}

            for billete, cantidad_disponible in billetes_disponibles.items():
                cantidad_billetes = min(monto_retiro // billete, cantidad_disponible)
                billetes_entregados[billete] = cantidad_billetes
                monto_retiro -= cantidad_billetes * billete

            if monto_retiro > 0:
                print("No se puede entregar el monto exacto con los billetes disponibles.")
            else:
                saldo_usuario -= monto_retiro
                saldo_cajero -= monto_retiro

                print("Saldo cuenta =", saldo_usuario)
                print("Saldo cajero =", saldo_cajero)

                for billete, cantidad in billetes_entregados.items():
                    print(f"billetes {billete}={cantidad}")

        opcion = input("¿Desea realizar otro retiro? (N para salir): ")
        if opcion.upper() != "N":
            break

    else:
        print("Usuario o clave incorrectos")
        intentos_fallidos += 1

        if intentos_fallidos == 3:
            print("Tarjeta bloqueada")
            break
