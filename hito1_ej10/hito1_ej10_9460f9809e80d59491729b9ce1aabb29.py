#Cajero Automático
saldo_inicial = 1000000
saldo_cajero = saldo_inicial
usuario_valido = 10334151
clave_valida = 1803
intentos_fallidos = 0

while True:
    usuario = int(input("Ingrese su número de usuario: "))
    clave = int(input("Ingrese su clave: "))

    if usuario == usuario_valido and clave == clave_valida:
        saldo_cuenta = 100000
        print("Inicio de sesión exitoso.")
        break
    else:
        intentos_fallidos += 1
        print("Clave inválida.")

    if intentos_fallidos >= 3:
        print("Tarjeta bloqueada. Por favor, contacte a su banco.")
        exit()

while True:
    monto_retiro = int(input("Ingrese el monto a retirar: "))

    if monto_retiro > saldo_cuenta:
        print("Monto no permitido. Fondos insuficientes.")
    elif monto_retiro > saldo_cajero:
        print("Monto no permitido. Cajero sin suficiente dinero.")
    else:
        saldo_cuenta -= monto_retiro
        saldo_cajero -= monto_retiro
        print("Retiro exitoso.")
        print("saldo cuenta=" + str(saldo_cuenta))
        print("saldo cajero=" + str(saldo_cajero))

    continuar = input("¿Desea realizar otra transacción? (S/N): ")
    if continuar.upper() != "S":
        break
