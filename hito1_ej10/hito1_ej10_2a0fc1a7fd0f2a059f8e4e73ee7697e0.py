#Cajero Automático
# Saldo inicial del cajero y usuario con acceso
saldo_cajero = 1000000
saldo_usuario = 100000

# Datos del usuario con acceso
usuario_valido = 10334151
clave_valida = 1803
intentos_fallidos = 0

# Función para retirar dinero de la cuenta del usuario
def retirar_dinero(monto):
    # Acceder a las variables globales
    global saldo_cajero, saldo_usuario

    # Validar que el monto a retirar sea menor o igual al saldo disponible
    if monto > saldo_usuario:
        print("Monto no permitido")
        return
    # Actualizar saldos
    saldo_cajero -= monto
    saldo_usuario -= monto

    # Imprimir nuevos saldos
    print("Saldo cuenta =", saldo_usuario)
    print("Saldo cajero =", saldo_cajero)

# Pedir usuario y clave para ingresar
usuario = int(input("Ingrese usuario: "))
clave = int(input("Ingrese clave: "))

# Validar usuario y clave
while usuario != usuario_valido or clave != clave_valida:
    intentos_fallidos += 1
    if intentos_fallidos >= 3:
        print("Tarjeta bloqueada")
        exit()
    print("Clave invalida")
    usuario = int(input("Ingrese usuario: "))
    clave = int(input("Ingrese clave: "))

# Pedir monto a retirar
monto_retiro = int(input("Ingrese monto a retirar: "))

# Retirar dinero de la cuenta del usuario
retirar_dinero(monto_retiro)
      