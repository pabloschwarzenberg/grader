#Cajero Automático
def validar_clave(usuario, clave):
    # Verificar el usuario y la clave
    if usuario == 10334151 and clave == 1803:
        return True
    else:
        return False

def retirar_dinero(monto, saldo_cuenta, saldo_cajero):
    # Verificar si el monto es válido
    if monto > 0 and monto <= saldo_cuenta:
        # Actualizar saldos
        saldo_cuenta -= monto
        saldo_cajero -= monto
        print("Retiro exitoso")
        print("Saldo cuenta = {}".format(saldo_cuenta))
        print("Saldo cajero = {}".format(saldo_cajero))
    else:
        print("Monto no permitido")

# Configuración inicial
saldo_cuenta = 100000
saldo_cajero = 1000000
intentos_fallidos = 0

# Pedir usuario y clave
usuario = int(input("Ingrese su usuario: "))
clave = int(input("Ingrese su clave: "))

# Validar usuario y clave
if validar_clave(usuario, clave):
    while True:
        monto = float(input("Ingrese el monto a retirar: "))

        # Verificar el monto
        if monto < 0:
            print("Monto no permitido")
        else:
            # Realizar el retiro
            retirar_dinero(monto, saldo_cuenta, saldo_cajero)
            break
else:
    print("Clave inválida")
    intentos_fallidos += 1

    # Verificar intentos fallidos
    if intentos_fallidos >= 3:
        print("Tarjeta bloqueada")











      