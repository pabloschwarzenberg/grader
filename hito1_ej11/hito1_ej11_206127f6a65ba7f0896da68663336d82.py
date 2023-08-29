def validar_clave(usuario, clave):
    if usuario == "10334151" and clave == "1803":
        return True
    else:
        return False

def retirar_dinero(saldo_cuenta, saldo_cajero, monto):
    if monto <= saldo_cuenta and monto <= saldo_cajero:
        saldo_cuenta -= monto
        saldo_cajero -= monto
        return saldo_cuenta, saldo_cajero
    else:
        return None

def distribuir_billetes(monto):
    billetes_20000 = monto // 20000
    monto = monto % 20000
    billetes_10000 = monto // 10000
    monto = monto % 10000
    billetes_5000 = monto // 5000
    monto = monto % 5000

    return billetes_20000, billetes_10000, billetes_5000

# Datos iniciales
saldo_cuenta = 100000
saldo_cajero = 1000000
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40
intentos_fallidos = 0

# Ingreso de usuario y clave
usuario = input("Ingrese su usuario: ")
clave = input("Ingrese su clave: ")

# Validar usuario y clave
if validar_clave(usuario, clave):
    while True:
        # Ingreso del monto a retirar
        try:
            monto = int(input("Ingrese el monto a retirar: "))
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un valor numérico.")
            continue

        # Verificar monto a retirar
        if monto <= 0:
            print("Monto no permitido")
        else:
            resultado = retirar_dinero(saldo_cuenta, saldo_cajero, monto)
            if resultado is not None:
                saldo_cuenta, saldo_cajero = resultado
                billetes_20000_retiro, billetes_10000_retiro, billetes_5000_retiro = distribuir_billetes(monto)
                print("Saldo cuenta:", saldo_cuenta)
                print("Saldo cajero:", saldo_cajero)
                print("Billetes 20000:", billetes_20000_retiro)
                print("Billetes 10000:", billetes_10000_retiro)
                print("Billetes 5000:", billetes_5000_retiro)
            else:
                print("Monto no permitido")

        # Salir del programa después de 3 intentos fallidos
        intentos_fallidos += 1
        if intentos_fallidos == 3:
            print("Tarjeta bloqueada")
            break
else:
    print("Clave inválida")
