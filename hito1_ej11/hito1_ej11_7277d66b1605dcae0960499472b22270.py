# Cajero Automático
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

usuario = input("Ingrese su usuario: ")
clave = input("Ingrese su clave: ")

if usuario == usuario_valido and clave == clave_valida:
    print("Bienvenido/a,", usuario)

    monto_retiro = int(input("Ingrese el monto a retirar: "))  # Modifica este valor según tus necesidades

    if monto_retiro > saldo_usuario or monto_retiro <= 0:
        print("Monto no permitido")
    else:
        billetes_entregados = {}
        total_entregado = 0

        for billete in sorted(billetes_disponibles.keys(), reverse=True):
            cantidad_disponible = billetes_disponibles[billete]
            cantidad_entregada = min(monto_retiro // billete, cantidad_disponible)
            monto_entregado = cantidad_entregada * billete
            billetes_entregados[billete] = cantidad_entregada
            billetes_disponibles[billete] -= cantidad_entregada
            total_entregado += monto_entregado
            monto_retiro -= monto_entregado

        if monto_retiro == 0:
            saldo_usuario -= total_entregado
            saldo_cajero -= total_entregado

            print("Saldo cuenta =", saldo_usuario)
            print("Saldo cajero =", saldo_cajero)
            print("Suma de billetes:", total_entregado)  # Imprime solo el valor numérico
        else:
            print("El cajero no tiene suficientes billetes para entregar el monto solicitado")

else:
    print("Usuario o clave incorrectos")
    intentos_fallidos += 1

    if intentos_fallidos == 3:
        print("Tarjeta bloqueada")
