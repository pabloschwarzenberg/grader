#Cajero Automático
saldo_cuenta = 100000  # Saldo inicial de la cuenta corriente
saldo_cajero = 1000000  # Saldo inicial del cajero automático

intentos_fallidos = 0  # Contador de intentos fallidos de inicio de sesión

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
    global saldo_cuenta, saldo_cajero

    if monto <= saldo_cuenta and monto <= saldo_cajero:
        saldo_cuenta -= monto
        saldo_cajero -= monto
        print("Saldo cuenta =", saldo_cuenta)
        print("Saldo cajero =", saldo_cajero)
    else:
        print("Monto no permitido.")

# Ingreso de usuario y clave
usuario_ingresado = input("Ingrese su usuario: ")
clave_ingresada = input("Ingrese su clave: ")

iniciar_sesion = validar_inicio_sesion(usuario_ingresado, clave_ingresada)

if iniciar_sesion:
    print("Bienvenido.")

    # Ingreso del monto de retiro
    monto = int(input("Ingrese el monto a retirar: "))
    retirar_dinero(monto)
