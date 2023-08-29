#Cajero Automático
def verificar_clave(usuario, clave):
    if usuario == "10334151" and clave == "1803":
        return True
    else:
        return False
def retirar_dinero(saldo_cuenta, billetes_20000, billetes_10000, billetes_5000):
   monto = int(input("Ingrese el monto a retirar: "))

    if monto <= saldo_cuenta:
        # Calcula la cantidad de billetes necesarios de cada denominación
        cant_20000 = min(billetes_20000, monto // 20000)
        monto -= cant_20000 * 20000

        cant_10000 = min(billetes_10000, monto // 10000)
        monto -= cant_10000 * 10000

        cant_5000 = min(billetes_5000, monto // 5000)
        monto -= cant_5000 * 5000

        if monto == 0:
            # Realiza el retiro y actualiza los saldos de billetes y cuenta
            saldo_cuenta -= (cant_20000 * 20000 + cant_10000 * 10000 + cant_5000 * 5000)
            billetes_20000 -= cant_20000
            billetes_10000 -= cant_10000
            billetes_5000 -= cant_5000

            print("Retiro exitoso.")
            print("Saldo cuenta:", saldo_cuenta)
            print("Billetes 20000:", cant_20000)
            print("Billetes 10000:", cant_10000)
            print("Billetes 5000:", cant_5000)
        else:
            print("Monto no permitido.")
    else:
        print("Saldo insuficiente.")


saldo_cuenta = 100000
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40
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
    retirar_dinero(saldo_cuenta, billetes_20000, billetes_10000, billetes_5000)
    continuar = input("¿Desea realizar otro retiro? (N para salir): ")

    if continuar.upper() == "N":
        break   