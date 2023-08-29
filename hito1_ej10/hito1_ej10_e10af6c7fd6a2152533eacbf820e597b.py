#Cajero Automático
saldo_cuenta = 100000
saldo_cajero = 1000000
intentos_fallidos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Bienvenido al cajero")
        break
    else:
        print("Usuario o clave incorrectos")
        intentos_fallidos += 1

    if intentos_fallidos == 3:
        print("Tarjeta bloqueada")
        exit()

while True:
    monto_retiro = int(input("Ingrese el monto a retirar: "))

    if monto_retiro <= 0 or monto_retiro > saldo_cuenta:
        print("Monto no permitido")
    else:
        saldo_cuenta -= monto_retiro
        saldo_cajero -= monto_retiro
        print("Retiro exitoso")
        print("saldo cuenta={}".format(saldo_cuenta))
        print("saldo cajero={}".format(saldo_cajero))

    continuar = input("¿Desea realizar otro retiro? (S/N): ")
    if continuar != "S":
        break
