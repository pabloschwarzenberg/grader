#Cajero Automático
saldo_inicial = 1000000
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40
usuario_valido = 10334151
clave_valida = 1803
intentos_fallidos = 0

while True:
    usuario = int(input("Ingrese su usuario: "))
    clave = int(input("Ingrese su clave: "))

    if usuario == usuario_valido and clave == clave_valida:
        saldo_usuario = 100000
        print("Inicio de sesión exitoso.")
        break
    else:
        print("Usuario o clave incorrectos.")
        intentos_fallidos += 1

    if intentos_fallidos == 3:
        print("Tarjeta bloqueada.")
        exit()

while True:
    monto_retiro = int(input("Ingrese el monto a retirar: "))

    if monto_retiro > saldo_usuario:
        print("Monto no permitido. Fondos insuficientes.")
    elif monto_retiro > saldo_inicial:
        print("Monto no permitido. Cajero sin fondos suficientes.")
    else:
        # Verificar si es posible distribuir los billetes de forma exacta
        if monto_retiro % 5000 != 0:
            print("Monto no permitido. No se puede distribuir en billetes exactos.")
            continue

        # Calcular la cantidad de billetes de cada denominación
        billetes_20000_retiro = min(billetes_20000, monto_retiro // 20000)
        billetes_10000_retiro = min(billetes_10000, (monto_retiro - billetes_20000_retiro * 20000) // 10000)
        billetes_5000_retiro = min(billetes_5000, (monto_retiro - billetes_20000_retiro * 20000 - billetes_10000_retiro * 10000) // 5000)

        # Actualizar saldos y billetes disponibles
        saldo_usuario -= monto_retiro
        saldo_inicial -= monto_retiro
        billetes_20000 -= billetes_20000_retiro
        billetes_10000 -= billetes_10000_retiro
        billetes_5000 -= billetes_5000_retiro

        print("Retiro exitoso.")
        print("Saldo cuenta= {}".format(saldo_usuario))
        print("Saldo cajero= {}".format(saldo_inicial))
        print("Billetes 20000= {}".format(billetes_20000_retiro))
        print("Billetes 10000= {}".format(billetes_10000_retiro))
        print("Billetes 5000= {}".format(billetes_5000_retiro))

    opcion = input("¿Desea realizar otro retiro? (S/N): ")
    if opcion.upper() != "S":
        break

