saldo_inicial = 1000000
saldo_cajero = 1000000
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
    saldo_cajero -= monto_retiro

    print("Saldo cuenta =", saldo_usuario)
    print("Saldo cajero =", saldo_cajero)

    opcion = input("¿Desea realizar otro retiro? (S/N): ")
    if opcion.upper() != "S":
        break
