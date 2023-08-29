#Cajero Automático
saldo_cuenta = 100000
saldo_cajero = 1000000
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40
intentos = 0

def realizar_retiro(monto):
    global saldo_cuenta, saldo_cajero, billetes_20000, billetes_10000, billetes_5000

    billetes_20000_retiro = min(monto // 20000, billetes_20000)
    monto -= billetes_20000_retiro * 20000
    billetes_10000_retiro = min(monto // 10000, billetes_10000)
    monto -= billetes_10000_retiro * 10000
    billetes_5000_retiro = min(monto // 5000, billetes_5000)
    monto -= billetes_5000_retiro * 5000

    if monto != 0:
        print("No se puede retirar el monto solicitado")
        return

    saldo_cuenta -= (billetes_20000_retiro * 20000) + (billetes_10000_retiro * 10000) + (billetes_5000_retiro * 5000)
    saldo_cajero -= (billetes_20000_retiro * 20000) + (billetes_10000_retiro * 10000) + (billetes_5000_retiro * 5000)

    print("Retiro exitoso")
    print("Saldo cuenta:", saldo_cuenta)
    print("Saldo cajero:", saldo_cajero)
    print("Billetes 20000:", billetes_20000_retiro)
    print("Billetes 10000:", billetes_10000_retiro)
    print("Billetes 5000:", billetes_5000_retiro)

    billetes_20000 -= billetes_20000_retiro
    billetes_10000 -= billetes_10000_retiro
    billetes_5000 -= billetes_5000_retiro

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Bienvenido")
        break
    else:
        print("Usuario o clave incorrectos")
        intentos += 1

    if intentos == 3:
        print("Tarjeta bloqueada")
        exit()

while True:
    monto_retiro = int(input("Ingrese el monto a retirar: "))

    if monto_retiro <= 0:
        print("Monto no permitido")
    elif monto_retiro > saldo_cuenta or monto_retiro > saldo_cajero:
        print("Saldo insuficiente")
    else:
        realizar_retiro(monto_retiro)

    respuesta = input("¿Desea realizar otro retiro? (S/N): ")
    if respuesta != "S" and respuesta != "s":
        break
