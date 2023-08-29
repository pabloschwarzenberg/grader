#Cajero Automático
saldo_inicial = 1000000
saldo_usuario = 100000
intentos_fallidos = 0

usuario_valido = 10334151
clave_valida = 1803

while True:
    usuario = int(input("Ingrese su usuario: "))
    clave = int(input("Ingrese su clave: "))

    if usuario == usuario_valido and clave == clave_valida:
        print("Inicio de sesión exitoso")
        break
    else:
        print("Usuario o clave incorrectos")
        intentos_fallidos += 1

    if intentos_fallidos == 3:
        print("Tarjeta bloqueada")
        exit()

while True:
    monto_retiro = int(input("Ingrese el monto a retirar: "))

    if monto_retiro <= saldo_usuario:
        if monto_retiro > 0:
            saldo_usuario -= monto_retiro
            saldo_inicial -= monto_retiro
            print("Retiro exitoso")
            print("Nuevo saldo en la cuenta corriente:", saldo_inicial)
            print("Nuevo saldo en la cuenta del usuario:", saldo_usuario)
        else:
            print("Monto no permitido")
    else:
        print("Fondos insuficientes")
