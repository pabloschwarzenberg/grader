saldo_cajero = 1000000
saldo_cuenta = 100000
usuario = "10334151"
clave_correcta = "1803"
intentos_fallidos = 0
billetes = {20000: 20, 10000: 40, 5000: 40}

while True:
    print("Bienvenido al cajero automático")
    usuario_ingresado = input("Ingresa tu usuario: ")
    if usuario_ingresado != usuario:
        print("Usuario incorrecto")
        continue

    clave_ingresada = input("Ingresa tu clave: ")
    if clave_ingresada != clave_correcta:
        intentos_fallidos += 1
        if intentos_fallidos == 3:
            print("Tarjeta bloqueada")
            break
        else:
            print("Clave invalida")
            continue

    monto = int(input("Ingresa el monto a retirar: "))
    if monto > saldo_cuenta or monto > saldo_cajero:
        print("Monto no permitido")
    else:
        saldo_cuenta -= monto
        saldo_cajero -= monto
        for valor, cantidad in billetes.items():
            num_billetes = min(cantidad, monto // valor)
            billetes[valor] -= num_billetes
            monto -= num_billetes * valor
            print("Billetes", valor ":", num_billetes)
        print("Saldo cuenta:", saldo_cuenta)
        print("Saldo cajero:", saldo_cajero)

    continuar = input("¿Deseas realizar otra operación? (N para salir): ")
    if continuar.upper() != "N":
        break
