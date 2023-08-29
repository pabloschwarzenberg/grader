usuario_valido = "10334151"
clave_valida = "1803"
saldo_cuenta = 100000
saldo_cajero = 1000000
intentos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == usuario_valido and clave == clave_valida:
        print("Acceso permitido")
        break
    else:
        intentos += 1
        if intentos >= 3:
            print("Tarjeta bloqueada")
            exit()
        else:
            print("Clave inválida")

while True:
    monto = float(input("Ingrese el monto a retirar: "))

    if monto <= 0:
        print("Monto no permitido")
    elif monto > saldo_cuenta:
        print("Saldo insuficiente")
    else:
        saldo_cuenta -= monto
        saldo_cajero -= monto
        print("Retiro exitoso")
        print("Saldo cuenta =", saldo_cuenta)
        print("Saldo cajero =", saldo_cajero)

    opcion = input("¿Desea realizar otro retiro? (S/N): ")
    if opcion.upper() != "S":
        break