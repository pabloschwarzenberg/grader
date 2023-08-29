saldo_cuenta = 100000
saldo_cajero = 1000000

billetes_disponibles = {
    20000: 20,
    10000: 40,
    5000: 40
}

intentos_fallidos = 0

def distribuir_billetes(monto):
    billetes = [20000, 10000, 5000]
    billetes_entregados = {}

    for billete in billetes:
        cantidad_billetes = min(int(monto // billete), billetes_disponibles[billete])
        billetes_disponibles[billete] -= cantidad_billetes
        monto -= cantidad_billetes * billete
        billetes_entregados[billete] = cantidad_billetes

    if monto > 0:
        print("No se pueden entregar todos los billetes solicitados")

    for billete, cantidad in billetes_entregados.items():
        print("billetes {} = {}".format(billete, cantidad))

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Acceso permitido")
        break
    else:
        intentos_fallidos += 1
        print("Clave inválida")

    if intentos_fallidos == 3:
        print("Tarjeta bloqueada")
        exit()

while True:
    monto = float(input("Ingrese el monto a retirar: "))

    if monto > saldo_cuenta:
        print("Monto no permitido")
    else:
        saldo_cuenta -= monto
        saldo_cajero -= monto
        print("Saldo cuenta =", saldo_cuenta)
        print("Saldo cajero =", saldo_cajero)
        distribuir_billetes(monto)

    opcion = input("¿Desea realizar otra transacción? (S/N): ")
    if opcion.upper() != "S":
        break
