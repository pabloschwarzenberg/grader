#Cajero Automático
saldo_cuenta = 100000
saldo_cajero = 1000000
intentos_fallidos = 0

# Validar usuario y clave
usuario = input("Ingrese su usuario: ")
clave = input("Ingrese su clave: ")

if usuario == "10334151" and clave == "1803":
    while intentos_fallidos < 3:
        monto_retiro = float(input("Ingrese el monto a retirar: "))

        # Validar monto a retirar
        if monto_retiro <= 0:
            print("Monto no permitido.")
        elif monto_retiro > saldo_cuenta:
            print("Saldo insuficiente.")
        else:
            saldo_cuenta -= monto_retiro
            saldo_cajero -= monto_retiro

            print("Retiro exitoso.")
            print("Saldo cuenta =", saldo_cuenta)
            print("Saldo cajero =", saldo_cajero)

            break
else:
    print("Usuario o clave inválida.")
    intentos_fallidos += 1

if intentos_fallidos == 3:
    print("Tarjeta bloqueada.")
