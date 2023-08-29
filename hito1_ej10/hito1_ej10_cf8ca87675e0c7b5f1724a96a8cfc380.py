#Cajero Automático
saldo_cuenta = 100000
saldo_cajero = 1000000
intentos_fallidos = 0

usuario_valido = 10334151
clave_valida = 1803

while True:
    usuario = int(input("Ingrese su número de usuario: "))
    clave = int(input("Ingrese su clave: "))

    if usuario == usuario_valido and clave == clave_valida:
        print("Acceso permitido")
        break
    else:
        print("Clave inválida")
        intentos_fallidos += 1

    if intentos_fallidos == 3:
        print("Tarjeta bloqueada")
        exit()

while True:
    monto_retiro = float(input("Ingrese el monto a retirar: "))

    if monto_retiro <= saldo_cuenta and monto_retiro % 1000 == 0:
        saldo_cuenta -= monto_retiro
        saldo_cajero -= monto_retiro
        print("Retiro exitoso")
        print("Saldo cuenta =", saldo_cuenta)
        print("Saldo cajero =", saldo_cajero)
        break
    else:
        print("Monto no permitido")
      