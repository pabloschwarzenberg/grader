#Cajero Automático
def verificar_clave(usuario, clave):
    if usuario == "10334151" and clave == "1803":
        return True
    else:
        return False

def realizar_retiro(monto, saldo_cuenta, saldo_cajero):
    if monto <= saldo_cuenta and monto <= saldo_cajero:
        saldo_cuenta -= monto
        saldo_cajero -= monto
        print("Retiro exitoso.")
        print("Saldo cuenta:", saldo_cuenta)
        print("Saldo cajero:", saldo_cajero)
    else:
        print("Monto no permitido.")

saldo_cuenta = 100000
saldo_cajero = 1000000
intentos_fallidos = 0

while True:
    usuario = input("Ingrese el usuario: ")
    clave = input("Ingrese la clave: ")

    if verificar_clave(usuario, clave):
        print("Bienvenido,", usuario)
        break
    else:
        intentos_fallidos += 1
        print("Clave inválida.")

    if intentos_fallidos >= 3:
        print("Tarjeta bloqueada.")
        exit()

while True:
    monto = float(input("Ingrese el monto a retirar: "))

    realizar_retiro(monto, saldo_cuenta, saldo_cajero)

    opcion = input("¿Desea realizar otro retiro? (S/N): ")
    if opcion.upper() != "S":
        break
      