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

# Datos iniciales
saldo_cuenta = 100000
saldo_cajero = 1000000
intentos_fallidos = 0

# Ingreso de usuario y clave
usuario = input("Ingrese su usuario: ")
clave = input("Ingrese su clave: ")

# Validar usuario y clave
if validar_clave(usuario, clave):
    while True:
        # Ingreso del monto a retirar
        monto = float(input("Ingrese el monto a retirar: "))

        # Verificar monto a retirar
        if monto <= 0:
            print("Monto no permitido")
        else:
            resultado = retirar_dinero(saldo_cuenta, saldo_cajero, monto)
            if resultado is not None:
                saldo_cuenta, saldo_cajero = resultado
                print("Saldo cuenta:", saldo_cuenta)
                print("Saldo cajero:", saldo_cajero)
            else:
                print("Monto no permitido")

        # Salir del programa después de 3 intentos fallidos
        intentos_fallidos += 1
        if intentos_fallidos == 3:
            print("Tarjeta bloqueada")
            break
else:
    print("Clave inválida")
