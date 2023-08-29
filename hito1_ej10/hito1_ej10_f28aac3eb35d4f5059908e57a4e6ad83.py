#Cajero Automático
def validar_usuario(usuario, clave):
    if usuario == "10334151" and clave == "1803":
        return True
    else:
        return False

def retirar_dinero(monto, saldo_cuenta, saldo_cajero):
    if monto <= saldo_cuenta and monto <= saldo_cajero:
        saldo_cuenta -= monto
        saldo_cajero -= monto
        return saldo_cuenta, saldo_cajero
    else:
        return None, saldo_cajero

# Saldo inicial
saldo_cuenta = 100000
saldo_cajero = 1000000

# Contadores de intentos y bloqueo
intentos = 0
bloqueado = False

while True:
    if bloqueado:
        print("Tarjeta bloqueada. Programa finalizado.")
        break

    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if validar_usuario(usuario, clave):
        print("Bienvenido.")

        while True:
            monto = float(input("Ingrese el monto a retirar: "))

            if monto < 0:
                print("Monto no permitido. Intente nuevamente.")
                continue

            saldo_cuenta, saldo_cajero = retirar_dinero(monto, saldo_cuenta, saldo_cajero)

            if saldo_cuenta is None:
                print("Monto no permitido. Intente nuevamente.")
                continue

            print("Retiro exitoso.")
            print("Saldo cuenta =", saldo_cuenta)
            print("Saldo cajero =", saldo_cajero)

            break

    else:
        intentos += 1
        if intentos >= 3:
            bloqueado = True
            print("Tarjeta bloqueada. Programa finalizado.")
        else:
            print("Clave inválida. Intente nuevamente.")

    opcion = input("¿Desea continuar? (S/N): ")
    if opcion.upper() != "S":
        break      