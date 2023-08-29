saldo_inicial = 1000000
saldo_cuenta = 100000
saldo_cajero = saldo_inicial
usuario_valido = 10334151
clave_valida = 1803
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
      monto = int(input("Ingrese el monto a retirar: "))
    if monto <= 0:
        print("Monto no permitido.")
    elif monto > saldo_cuenta:
        print("Saldo insuficiente.")
    elif monto > saldo_cajero:
        print("El cajero no dispone de suficiente efectivo.")
    else:
        saldo_cuenta -= monto
        saldo_cajero -= monto
        print("Retiro exitoso.")
        print("Saldo cuenta: {}".format(saldo_cuenta))
        print("Saldo cajero: {}".format(saldo_cajero))
    opcion = input("¿Desea realizar otro retiro? (N para salir): ")
    if opcion.upper() == "N":
        break
