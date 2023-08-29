#Cajero Automático
saldo_cuenta = 1000000
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

def realizar_retiro(monto):
    global saldo_cuenta, billetes_20000, billetes_10000, billetes_5000

    if monto > saldo_cuenta:
        print("Saldo insuficiente.")
        return

    if monto % 5000 != 0:
        print("Monto no válido.")
        return

    if monto > billetes_20000 * 20000 + billetes_10000 * 10000 + billetes_5000 * 5000:
        print("No hay suficientes billetes para el monto solicitado.")
        return

    billetes_20000_retirados = min(monto // 20000, billetes_20000)
    monto -= billetes_20000_retirados * 20000
    billetes_20000 -= billetes_20000_retirados

    billetes_10000_retirados = min(monto // 10000, billetes_10000)
    monto -= billetes_10000_retirados * 10000
    billetes_10000 -= billetes_10000_retirados

    billetes_5000_retirados = min(monto // 5000, billetes_5000)
    monto -= billetes_5000_retirados * 5000
    billetes_5000 -= billetes_5000_retirados

    saldo_cuenta -= (billetes_20000_retirados * 20000 + billetes_10000_retirados * 10000 + billetes_5000_retirados * 5000)

    print("Retiro exitoso.")
    print("Saldo en cuenta:", saldo_cuenta)
    print("Billetes entregados:")
    print("Billetes de 20000:", billetes_20000_retirados)
    print("Billetes de 10000:", billetes_10000_retirados)
    print("Billetes de 5000:", billetes_5000_retirados)

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Bienvenido, usuario.")
        break
    else:
        print("Usuario o clave incorrectos. Intente nuevamente.")

intentos = 0

while intentos < 3:
    monto_retiro = int(input("Ingrese el monto a retirar: "))

    realizar_retiro(monto_retiro)

    intentos += 1

    if intentos == 3:
        print("Tarjeta bloqueada.")
        break

    opcion = input("¿Desea realizar otro retiro? (S/N): ")
    if opcion.upper() != "S":
        break

print("Gracias por utilizar nuestro cajero automático. Hasta luego!")
