saldo_inicial_cajero = 1000000
saldo_inicial_cuenta = 100000
intentos_fallidos = 0

def verificar_clave(usuario, clave):
    if usuario == 10334151 and clave == 1803:
        return True
    else:
        return False

def retirar_dinero(monto):
    global saldo_inicial_cuenta, saldo_inicial_cajero
    if monto <= saldo_inicial_cuenta:
        if monto <= saldo_inicial_cajero:
            saldo_inicial_cuenta -= monto
            saldo_inicial_cajero -= monto
            print("Retiro exitoso.")
            print("Nuevo saldo en la cuenta: saldo cuenta =", saldo_inicial_cuenta)
            print("Nuevo saldo en el cajero: saldo cajero =", saldo_inicial_cajero)
        else:
            print("Monto no permitido. Saldo insuficiente en el cajero.")
    else:
        print("Monto no permitido. Saldo insuficiente en la cuenta.")

while intentos_fallidos < 3:
    usuario = int(input("Ingrese su número de usuario: "))
    clave = int(input("Ingrese su clave: "))

    if verificar_clave(usuario, clave):
        monto_retiro = float(input("Ingrese el monto a retirar: "))
        retirar_dinero(monto_retiro)
        break
    else:
        print("Clave inválida.")
        intentos_fallidos += 1

if intentos_fallidos == 3:
    print("Tarjeta bloqueada. Por favor, contacte al banco.")
