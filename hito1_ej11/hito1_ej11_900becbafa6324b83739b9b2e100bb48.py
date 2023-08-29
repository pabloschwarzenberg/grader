#Cajero Automático
saldo_inicial = 1000000
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

usuario_valido = 10334151
clave_valida = 1803
saldo_usuario = 100000
saldo_cuenta = 100000
saldo_cajero = 1000000
intentos_malos = 0

def imprimir_distribucion_billetes(cantidad_20000, cantidad_10000, cantidad_5000):
    print("Distribución de billetes:")
    print("Billetes de 20000:", cantidad_20000)
    print("Billetes de 10000:", cantidad_10000)
    print("Billetes de 5000:", cantidad_5000)

while True:
    usuario = int(input("Ingrese el usuario: "))
    clave = int(input("Ingrese la clave: "))

    if usuario == usuario_valido and clave == clave_valida:
        print("Bienvenido al cajero automático")
        break
    else:
        print("clave incorrrecta o usuario")
        intentos_malos += 1
        if intentos_malos >= 3:
            print("Tarjeta bloqueada.")
            exit()

while True:
    monto_retiro = int(input("Ingrese el monto a retirar: "))

    if monto_retiro <= 0:
        print("Monto no permitido.")
    elif monto_retiro > saldo_usuario:
        print("Saldo insuficiente.")
    else:
        # Verificar si hay suficientes billetes para la distribución
        if monto_retiro % 5000 != 0:
            print("No es posible entregar el monto solicitado.")
        else:
            # Calcular la cantidad de billetes de cada denominación
            cantidad_20000 = min(billetes_20000, monto_retiro // 20000)
            cantidad_10000 = min(billetes_10000, (monto_retiro - cantidad_20000 * 20000) // 10000)
            cantidad_5000 = min(billetes_5000, (monto_retiro - cantidad_20000 * 20000 - cantidad_10000 * 10000) // 5000)

            # Actualizar saldos y cantidad de billetes disponibles
            saldo_usuario -= monto_retiro
            saldo_cajero -= monto_retiro
            billetes_20000 -= cantidad_20000
            billetes_10000 -= cantidad_10000
            billetes_5000 -= cantidad_5000

            print("el retiro fue un exito")
            print("Saldo en la cuenta:", saldo_usuario)
            print("Saldo en cajero:", saldo_cajero)
            imprimir_distribucion_billetes(cantidad_20000, cantidad_10000, cantidad_5000)

    continuar = input("¿Desea realizar otra transacción? apreta N para poder salir:")
    if continuar.upper() != "N":
        break     