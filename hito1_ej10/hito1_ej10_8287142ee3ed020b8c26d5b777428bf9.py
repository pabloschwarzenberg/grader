monto = 0
saldocuenta = 100000  # Saldo inicial de la cuenta
saldocajero = 1000000
intentos = 0

def validar_clave(usuario, clave):
    if usuario == "10334151" and clave == 1803:
        return True
    else:
        return False

def retirar_dinero(saldocuenta, monto):
    if monto > saldocuenta or monto <= 0:
        return False
    else:
        return True

# Bucle principal
while True:
    usuario = input("Ingrese el número de usuario: ")
    clave = int(input("Ingrese la clave: "))

    # Validar la clave del usuario
    if validar_clave(usuario, clave):
        print("Clave válida.")
        intentos = 0
        monto = int(input("Ingrese el monto a retirar: "))

        # Realizar retiro de dinero
        if monto <= 100000:
            if retirar_dinero(saldocuenta, monto):
                print("Monto retirado:", monto)
                saldocuenta -= monto
                saldocajero -= monto
                print("Retiro exitoso.")
                print("Saldo cuenta: ", saldocuenta)
                print("Saldo cajero: ",saldocajero )
                # No se actualiza el saldo del cajero, ya que no se especifica cómo se gestiona
            else:
                print("No es posible retirar el monto especificado.")
        else:
            print("Monto no permitido.")

    else:
        intentos += 1
        print("Clave inválida.")

        # Verificar si se superó el límite de intentos
        if intentos == 3:
            print("Tarjeta bloqueada.")
            break

    continuar = input("¿Desea realizar otra transacción? (S/N): ")
    if continuar.upper() != "S":
        break