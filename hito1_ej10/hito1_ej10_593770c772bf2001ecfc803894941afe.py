#Cajero Automático
def verificar_clave(usuario, clave):
    if usuario == "10334151" and clave == "1803":
        return True
    else:
        return False

def retirar_dinero(saldo_cuenta, saldo_cajero):
    monto = float(input("Ingrese el monto a retirar: "))

    if monto <= saldo_cuenta:
        saldo_cuenta -= monto
        saldo_cajero -= monto
        print("Retiro exitoso.")
        print("Saldo cuenta:", saldo_cuenta)
        print("Saldo cajero:", saldo_cajero)
    else:
        print("Monto no permitido. Fondos insuficientes.")

    return saldo_cuenta, saldo_cajero

usuario = input("Ingrese el número de usuario: ")
clave = input("Ingrese la clave: ")

intentos = 1
saldo_cuenta = 100000
saldo_cajero = 1000000

while intentos <= 3:
    if verificar_clave(usuario, clave):
        print("Bienvenido,", usuario)
        print("Saldo cuenta:", saldo_cuenta)
        print("Saldo cajero:", saldo_cajero)
        opcion = input("¿Desea realizar un retiro? (S/N): ")

        if opcion.upper() == "S":
            saldo_cuenta, saldo_cajero = retirar_dinero(saldo_cuenta, saldo_cajero)

        usuario = input("Ingrese el número de usuario: ")
        clave = input("Ingrese la clave: ")
        intentos = 1
    else:
        print("Clave inválida.")
        intentos += 1

    if intentos > 3:
        print("Tarjeta bloqueada.")
        break

    continuar = input("¿Desea realizar otra transacción? (S/N): ")
    if continuar.upper() != "S":
        break
      