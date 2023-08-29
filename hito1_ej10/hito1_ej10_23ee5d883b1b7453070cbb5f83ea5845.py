saldo_inicial_cajero = 1000000
saldo_inicial_usuario = 100000
intentos_fallidos = 0

def ingresar_usuario():
    return input("Ingrese su usuario: ")

def ingresar_clave():
    return input("Ingrese su clave: ")

def validar_usuario(usuario):
    return usuario == "10334151"

def validar_clave(clave):
    return clave == "1803"

def verificar_saldo_suficiente(saldo, monto):
    return saldo >= monto

def realizar_retiro(saldo, monto):
    return saldo - monto

def actualizar_cajero(monto):
    global saldo_inicial_cajero
    saldo_inicial_cajero -= monto

def bloquear_tarjeta():
    global intentos_fallidos
    intentos_fallidos = 0
    print("Tarjeta bloqueada. Contacte al banco.")

def imprimir_saldos(saldo_usuario, saldo_cajero):
    print("saldo cuenta=" + str(saldo_usuario))
    print("saldo cajero=" + str(saldo_cajero))

def cajero_automatico():
    global intentos_fallidos

    usuario = ingresar_usuario()
    clave = ingresar_clave()

    if validar_usuario(usuario) and validar_clave(clave):
        saldo_usuario = saldo_inicial_usuario
        intentos_fallidos = 0

        while True:
            monto = int(input("Ingrese el monto a retirar: "))

            if monto <= 0:
                print("Monto no permitido")
                continue

            if verificar_saldo_suficiente(saldo_usuario, monto):
                saldo_usuario = realizar_retiro(saldo_usuario, monto)
                actualizar_cajero(monto)
                imprimir_saldos(saldo_usuario, saldo_inicial_cajero)
            else:
                print("Saldo insuficiente")
                continue

            opcion = input("¿Desea realizar otro retiro? (S/N): ")

            if opcion.upper() != "S":
                break
    else:
        intentos_fallidos += 1
        print("Clave inválida")

        if intentos_fallidos == 3:
            bloquear_tarjeta()

cajero_automatico()