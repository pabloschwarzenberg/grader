saldo_cajero = 1000000  # Saldo inicial del cajero
saldo_usuario = 100000  # Saldo inicial del usuario

intentos_fallidos = 0  # Contador de intentos fallidos de inicio de sesión

# Definición del usuario y clave válidos
usuario_valido = 10334151
clave_valida = 1803

# Bucle principal
while True:
    # Solicitar usuario y clave
    usuario = int(input("Ingrese su usuario: "))
    clave = int(input("Ingrese su clave: "))

    # Verificar usuario y clave
    if usuario == usuario_valido and clave == clave_valida:
        print("Inicio de sesión exitoso.")
        break  # Salir del bucle si la autenticación es exitosa

    print("Usuario o clave incorrectos.")
    intentos_fallidos += 1

    # Verificar límite de intentos fallidos
    if intentos_fallidos >= 3:
        print("Tarjeta bloqueada.")
        exit()  # Salir del programa si se supera el límite de intentos fallidos

# Si se llega a este punto, el usuario ha iniciado sesión exitosamente
while True:
    # Mostrar saldo actual
    print("Saldo cuenta =", saldo_usuario)
    print("Saldo cajero =", saldo_cajero)

    # Solicitar monto a retirar
    monto = int(input("Ingrese el monto a retirar: "))

    # Validar el monto a retirar
    if monto <= 0 or monto > saldo_usuario or monto > saldo_cajero:
        print("Monto no permitido.")
    else:
        # Actualizar saldos
        saldo_usuario -= monto
        saldo_cajero -= monto
        print("Retiro exitoso.")
        print("Saldo cuenta =", saldo_usuario)
        print("Saldo cajero =", saldo_cajero)
        break  # Salir del bucle si el retiro es exitoso

      