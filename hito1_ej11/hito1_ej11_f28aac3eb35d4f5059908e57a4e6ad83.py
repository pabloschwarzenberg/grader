#Cajero Automático
def validar_usuario(usuario, clave):
    if usuario == "10334151" and clave == "1803":
        return True
    else:
        return False

def contar_billetes(monto, denominacion, saldo_cajero):
    cantidad_billetes = monto // denominacion
    if cantidad_billetes <= saldo_cajero:
        saldo_cajero -= cantidad_billetes
        return cantidad_billetes, saldo_cajero
    else:
        return None, saldo_cajero

# Saldo inicial
saldo_cuenta = 100000
saldo_cajero = {
    20000: 20,
    10000: 40,
    5000: 40
}

# Contadores de intentos y bloqueo
intentos = 0
bloqueado = False

while True:
    if bloqueado:
        print("Tarjeta bloqueada. Programa finalizado.")
        break

    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if validar_usuario(usuario, clave):
        print("Bienvenido.")

        while True:
            monto = float(input("Ingrese el monto a retirar: "))

            if monto < 0:
                print("Monto no permitido. Intente nuevamente.")
                continue

            # Distribución de billetes
            billetes_entregados = {}
            for denominacion in sorted(saldo_cajero.keys(), reverse=True):
                cantidad, saldo_cajero[denominacion] = contar_billetes(monto, denominacion, saldo_cajero[denominacion])
                if cantidad is not None:
                    billetes_entregados[denominacion] = cantidad
                    monto -= cantidad * denominacion

            if monto != 0:
                print("Monto no permitido. Intente nuevamente.")
                continue

            print("Retiro exitoso.")
            print("Saldo cuenta =", saldo_cuenta)
            print("Saldo cajero =", sum(saldo_cajero.values()))

            # Imprimir billetes entregados
            print("Billetes entregados:")
            for denominacion, cantidad in billetes_entregados.items():
                print("Billetes", denominacion, "=", cantidad)

            break

    else:
        intentos += 1
        if intentos >= 3:
            bloqueado = True
            print("Tarjeta bloqueada. Programa finalizado.")
        else:
            print("Clave inválida. Intente nuevamente.")

    opcion = input("¿Desea continuar? (S/N): ")
    if opcion.upper() != "S":
        break      