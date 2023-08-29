#Cajero Automático
saldo_inicial = 1000000
saldo_cajero = saldo_inicial

usuario_valido = 10334151
clave_valida = 1803
saldo_usuario = 100000

intentos_fallidos = 0

while True:
    usuario = int(input("Ingrese su usuario: "))
    clave = int(input("Ingrese su clave: "))

    if usuario == usuario_valido and clave == clave_valida:
        print("Inicio de sesión exitoso.")
        break
    else:
        intentos_fallidos += 1
        print("Clave inválida.")

    if intentos_fallidos == 3:
        print("Tarjeta bloqueada.")
        exit()

while True:
    monto_retiro = int(input("Ingrese el monto a retirar: "))

    if monto_retiro > saldo_usuario:
        print("Monto no permitido.")
    else:
        saldo_usuario -= monto_retiro
        saldo_cajero -= monto_retiro
        print("Saldo cuenta =", saldo_usuario)
        print("Saldo cajero =", saldo_cajero)
        break
