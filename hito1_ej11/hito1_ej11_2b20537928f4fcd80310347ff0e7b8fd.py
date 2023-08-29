saldo_inicial = 1000000
saldo_cajero = {
    20000: 20,
    10000: 40,
    5000: 40
}

intentos = 0
usuario_valido = 10334151
clave_valida = 1803
saldo_usuario = 100000

while True:
    usuario = int(input("Ingrese su número de usuario: "))
    clave = int(input("Ingrese su clave: "))

    if usuario == usuario_valido and clave == clave_valida:
        print("Inicio de sesión exitoso")
        break
    else:
        print("Clave inválida")
        intentos += 1

    if intentos == 3:
        print("Tarjeta bloqueada")
        exit()

while True:
    monto_retiro = float(input("Ingrese el monto a retirar: "))

    if monto_retiro <= 0:
        print("Monto no permitido")
        continue

    if monto_retiro > saldo_usuario:
        print("Saldo insuficiente")
        continue

    saldo_usuario -= monto_retiro

    billetes_entregados = {}
    for billete, cantidad in saldo_cajero.items():
        if monto_retiro >= billete and cantidad > 0:
            cant_billetes = min(int(monto_retiro / billete), cantidad)
            monto_retiro -= billete * cant_billetes
            saldo_cajero[billete] -= cant_billetes
            billetes_entregados[billete] = cant_billetes

    if monto_retiro > 0:
        print("No se pueden entregar los billetes exactos")
        continue

    print("Billetes entregados:")
    for billete, cantidad in billetes_entregados.items():
        print("Billetes", billete, "=", cantidad)

    print("Saldo cuenta =", saldo_usuario)
    print("Saldo cajero =", saldo_cajero)

    opcion = input("¿Desea realizar otro retiro? (S/N): ")
    if opcion.upper() != "S":
        break
