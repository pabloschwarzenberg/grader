#Cajero Automático 2
def validar_clave(usuario, clave):
    if usuario == 10334151 and clave == 1803:
        return True
    else:
        return False

def retirar_dinero(saldo, monto):
  if monto > saldo or monto <= 0:
    return False
  else:
    return True

def distribuir_billetes(monto):
    billetes_20000 = monto // 20000
    monto = monto % 20000
    billetes_10000 = monto // 10000
    monto = monto % 10000
    billetes_5000 = monto // 5000
    return billetes_20000, billetes_10000, billetes_5000

# Saldo inicial del cajero y del usuario
saldo_cajero = 1000000
saldo_cuenta = 100000
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

# Intentos de ingreso de la clave
intentos = 0

# Bucle principal
while True:
    usuario = int(input("Ingrese el número de usuario: "))
    clave = int(input("Ingrese la clave: "))

    # Validar la clave del usuario
    if validar_clave(usuario, clave):
        print("Clave válida.")
        intentos = 0

        monto = float(input("Ingrese el monto a retirar: "))

        # Realizar retiro de dinero
        if retirar_dinero(saldo_cuenta, monto):
            saldo_cuenta -= monto
            saldo_cajero -= monto
            billetes_20000_retirados, billetes_10000_retirados, billetes_5000_retirados = distribuir_billetes(monto)
            billetes_20000 -= billetes_20000_retirados
            billetes_10000 -= billetes_10000_retirados
            billetes_5000 -= billetes_5000_retirados

            print("Retiro exitoso.")
            print("Saldo cuenta:", saldo_cuenta)
            print("Saldo cajero:", saldo_cajero)
            print("Billetes de 20.000 entregados:", billetes_20000_retirados)
            print("Billetes de 10.000 entregados:", billetes_10000_retirados)
            print("Billetes de 5.000 entregados:", billetes_5000_retirados)
        else:
            print("Monto no permitido.")
    else:
        intentos += 1
        print("Clave inválida.")
  
distribuir_billetes(monto)

    # Verificar si se superó el límite de intentos
  if intentos == 3:
        print("Tarjeta bloqueada.")
        break

    continuar = input("¿Desea realizar otra transacción? (S/N): ")
    if continuar.upper() != "S":
        break