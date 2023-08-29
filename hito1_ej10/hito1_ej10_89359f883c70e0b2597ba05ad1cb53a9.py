def verificar_clave(usuario, clave):
    if usuario == "10334151" and clave == "1803":
        return True
    else:
        return False

def retirar_dinero(saldo_cuenta, saldo_cajero):
monto = float(input("Ingrese el monto a retirar: "))

    if monto <= saldo_cuenta and monto % 10000 == 0:
        saldo_cuenta -= monto
        saldo_cajero -= monto
        print("Retiro exitoso.")
        print("Saldo cuenta:", saldo_cuenta)
        print("Saldo cajero:", saldo_cajero)
    else:
        print("Monto no permitido.")


saldo_cuenta = 100000
saldo_cajero = 1000000
intentos = 0

while True:
    usuario = input("Ingrese el número de usuario: ")
    clave = input("Ingrese la clave: ")

    if verificar_clave(usuario, clave):
        print("Acceso autorizado.")
        break
        else:
        intentos += 1
        print("Clave inválida.")

    if intentos == 3:
        print("Tarjeta bloqueada.")
        break

while True:
    retirar_dinero(saldo_cuenta, saldo_cajero)
    continuar = input("¿Desea realizar otro retiro? (N para salir): ")

    if continuar.upper() == "N":
        break