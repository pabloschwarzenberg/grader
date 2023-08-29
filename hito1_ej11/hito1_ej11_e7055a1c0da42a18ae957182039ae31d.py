#Cajero Automático
saldo_cajero = {
    20000: 20,
    10000: 40,
    5000: 40
}

def retirar_dinero(monto):
    global saldo_cajero
    
    # Verificar si el monto es válido
    if monto % 5000 != 0:
        print("Monto no permitido")
        return

    # Verificar si hay suficiente saldo en el cajero
    saldo_total = sum(billetes * valor for valor, billetes in saldo_cajero.items())
    if monto > saldo_total:
        print("Saldo insuficiente en el cajero")
        return

    # Realizar el retiro
    billetes_entregados = {}
    for valor, cantidad_disponible in saldo_cajero.items():
        cantidad_billetes = min(monto // valor, cantidad_disponible)
        billetes_entregados[valor] = cantidad_billetes
        monto -= valor * cantidad_billetes
        saldo_cajero[valor] -= cantidad_billetes

    # Imprimir los saldos actualizados
    print("Saldo cuenta:", saldo_cuenta)
    print("Saldo cajero:")
    for valor, cantidad_disponible in saldo_cajero.items():
        print("billetes", valor, "=", cantidad_disponible)

    # Imprimir los billetes entregados
    print("Billetes entregados:")
    for valor, cantidad in billetes_entregados.items():
        print("billetes", valor, "=", cantidad)

# Datos iniciales
saldo_cuenta = 1000000

# Solicitar al usuario ingresar la clave y el monto a retirar
clave = input("Ingrese su clave: ")
monto = int(input("Ingrese el monto a retirar: "))

# Verificar la clave
if clave != "1803":
    print("Clave inválida")
else:
    # Verificar el saldo y realizar el retiro
    if monto > saldo_cuenta:
        print("Saldo insuficiente en la cuenta")
    else:
        saldo_cuenta -= monto
        retirar_dinero(monto)
      