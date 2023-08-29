#Cajero Automático
saldo_cuenta = 100000  # Saldo inicial de la cuenta corriente
saldo_cajero = 1000000  # Saldo inicial del cajero automático

intentos_fallidos = 0  # Contador de intentos fallidos de inicio de sesión

billetes_20000 = 20  # Cantidad de billetes de 20000 disponibles
billetes_10000 = 40  # Cantidad de billetes de 10000 disponibles
billetes_5000 = 40  # Cantidad de billetes de 5000 disponibles

# Función para validar el inicio de sesión
def validar_inicio_sesion(usuario_ingresado, clave_ingresada):
    global intentos_fallidos

    usuario = "10334151"
    clave = "1803"

    if usuario_ingresado == usuario and clave_ingresada == clave:
        return True
    else:
        intentos_fallidos += 1
        if intentos_fallidos == 3:
            print("Tarjeta bloqueada")
            return False
        else:
            print("Clave inválida")
            return False

# Función para realizar un retiro de dinero
def retirar_dinero(monto):
    global saldo_cuenta, saldo_cajero, billetes_20000, billetes_10000, billetes_5000

    if monto <= saldo_cuenta and monto <= saldo_cajero:
        if monto % 5000 != 0:
            print("Monto no permitido. El monto debe ser múltiplo de 5000.")
            return

        if monto > (billetes_20000 * 20000) + (billetes_10000 * 10000) + (billetes_5000 * 5000):
            print("No hay suficientes billetes en el cajero.")
            return

        billetes_20000_entregados = min(monto // 20000, billetes_20000)
        monto -= billetes_20000_entregados * 20000
        billetes_10000_entregados = min(monto // 10000, billetes_10000)
        monto -= billetes_10000_entregados * 10000
        billetes_5000_entregados = min(monto // 5000, billetes_5000)

        saldo_cuenta -= (billetes_20000_entregados * 20000 +
                         billetes_10000_entregados * 10000 +
                         billetes_5000_entregados * 5000)
        saldo_cajero -= (billetes_20000_entregados * 20000 +
                         billetes_10000_entregados * 10000 +
                         billetes_5000_entregados * 5000)
        billetes_20000 -= billetes_20000_entregados
        billetes_10000 -= billetes_10000_entregados
        billetes_5000 -= billetes_5000_entregados

        print("Saldo cuenta =", saldo_cuenta)
        print("Saldo cajero =", saldo_cajero)
        print("Billetes 20000 =", billetes_20000_entregados)
        print("Billetes 10000 =", billetes_10000_entregados)
        print("Billetes 5000 =", billetes_5000_entregados)
    else:
        print("Monto no permitido. Saldo insuficiente.")

# Ingreso de usuario y clave
usuario_ingresado = input("Ingrese su usuario: ")
clave_ingresada = input("Ingrese su clave: ")

iniciar_sesion = validar_inicio_sesion(usuario_ingresado, clave_ingresada)

if iniciar_sesion:
    print("Bienvenido.")

    # Ingreso del monto de retiro
    monto = int(input("Ingrese el monto a retirar: "))
    retirar_dinero(monto)
