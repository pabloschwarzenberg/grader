#Cajero Automático

saldo_cuenta = 100000
saldo_cajero = 1000000
intentos_fallidos = 0

while intentos_fallidos < 3:
    usuario = input("Ingrese el número de usuario: ")
    clave = input("Ingrese la clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Bienvenido.")
        break
    else:
        print("Usuario o clave inválida.")
        intentos_fallidos += 1

    if intentos_fallidos == 3:
        print("Tarjeta bloqueada. Ha excedido el número de intentos permitidos.")
        exit()

while True:
    monto = float(input("Ingrese el monto a retirar: "))

    if monto <= 0 or monto > saldo_cuenta or monto > saldo_cajero:
        print("Monto no permitido.")
    else:
        saldo_cuenta -= monto
        saldo_cajero -= monto
        print("Retiro exitoso.")
        print("Saldo cuenta={}".format(saldo_cuenta))
        print("Saldo cajero={}".format(saldo_cajero))

    if input("¿Desea realizar otro retiro? (S/N): ").upper() != "S":
        break