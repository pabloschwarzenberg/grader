#Cajero Automático
saldo_inicial = 1000000
saldo_cuenta = 100000
saldo_cajero = {
    20000: 20,
    10000: 40,
    5000: 40
}
intentos_fallidos = 0

def verificar_usuario(usuario, clave):
    return usuario == "10334151" and clave == "1803"

def bloquear_tarjeta():
    print("Tarjeta bloqueada.")
    exit()

def actualizar_saldos(monto_retiro):
    global saldo_cuenta
    global saldo_cajero

    saldo_cuenta -= monto_retiro
    saldo_cajero_total = sum(denominacion * cantidad for denominacion, cantidad in saldo_cajero.items())
    saldo_cajero_total -= monto_retiro

    if saldo_cajero_total < 0:
        print("Monto no permitido. No hay suficientes billetes disponibles.")
        saldo_cuenta += monto_retiro  # Revertir el retiro
        return False

    saldo_cajero_copy = saldo_cajero.copy()

    for denominacion in sorted(saldo_cajero_copy.keys(), reverse=True):
        cantidad_billetes = min(monto_retiro // denominacion, saldo_cajero_copy[denominacion])
        monto_retiro -= cantidad_billetes * denominacion
        saldo_cajero[denominacion] -= cantidad_billetes
        print("billetes {}={}".format(denominacion, cantidad_billetes))

    return True

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if verificar_usuario(usuario, clave):
        print("¡Bienvenido!")
        break
    else:
        print("Usuario o clave incorrectos.")
        intentos_fallidos += 1

    if intentos_fallidos == 3:
        bloquear_tarjeta()

while True:
    monto_retiro = int(input("Ingrese el monto a retirar: "))

    if monto_retiro <= 0:
        print("Monto no permitido.")
    else:
        if monto_retiro > saldo_cuenta:
            print("Monto no permitido. Saldo insuficiente en la cuenta.")
        else:
            print("Retiro exitoso.")
            if not actualizar_saldos(monto_retiro):
                saldo_cuenta += monto_retiro  # Revertir el retiro

            print("saldo cuenta=" + str(saldo_cuenta))
            print("saldo cajero=" + str(sum(saldo_cajero.values())))

    continuar = input("¿Desea realizar otro retiro? (S/N): ")
    if continuar.upper() != "S":
        break