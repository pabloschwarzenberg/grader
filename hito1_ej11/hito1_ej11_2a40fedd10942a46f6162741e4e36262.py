saldo_inicial_cajero = {
    20000: 20,
    10000: 40,
    5000: 40
}

saldo_inicial_usuario = 100000
intentos_fallidos = 0

def validar_clave(usuario, clave):
    if usuario == '10334151' and clave == '1803':
        return True
    else:
        return False

def contar_billetes(monto, saldo_cajero):
    billetes_entregados = {}
    saldo_cajero_actualizado = saldo_cajero.copy()

    for valor_billete, cantidad_billetes in saldo_cajero_actualizado.items():
        if monto >= valor_billete:
            cantidad = min(monto // valor_billete, cantidad_billetes)
            monto -= valor_billete * cantidad
            billetes_entregados[valor_billete] = cantidad
            saldo_cajero_actualizado[valor_billete] -= cantidad

    if monto == 0:
        return billetes_entregados, saldo_cajero_actualizado
    else:
        return {}, saldo_cajero

def retirar_dinero(monto, saldo_usuario, saldo_cajero):
    if monto > saldo_usuario:
        print("Monto no permitido. Saldo insuficiente.")
    elif monto > sum(saldo_cajero.keys()):
        print("Monto no permitido. Cajero sin suficiente dinero.")
    else:
        saldo_usuario -= monto
        billetes_entregados, saldo_cajero_actualizado = contar_billetes(monto, saldo_cajero)

        if sum(billetes_entregados.values()) == 0:
            print("No se pudo realizar el retiro. No hay suficientes billetes para entregar el monto solicitado.")
        else:
            print("Retiro exitoso.")
            print("Saldo cuenta=", saldo_usuario)
            print("Saldo cajero=", saldo_cajero_actualizado)
            for valor_billete, cantidad in billetes_entregados.items():
                print("billetes", valor_billete, "=", cantidad)

        return saldo_usuario, saldo_cajero_actualizado

usuario = input("Ingrese su usuario: ")
clave = input("Ingrese su clave: ")

if validar_clave(usuario, clave):
    saldo_usuario = saldo_inicial_usuario
    saldo_cajero = saldo_inicial_cajero
    print("Bienvenido(a) al cajero automático.")

    while True:
        monto = int(input("Ingrese el monto a retirar: "))
        saldo_usuario, saldo_cajero = retirar_dinero(monto, saldo_usuario, saldo_cajero)

        opcion = input("¿Desea realizar otro retiro? (S/N): ")
        if opcion.upper() != 'S':
            break
else:
    print("Clave inválida. Intento fallido.")
    intentos_fallidos += 1

    if intentos_fallidos >= 3:
        print("Tarjeta bloqueada. Ha alcanzado el máximo de intentos permitidos.")

print("Gracias por utilizar el cajero automático. ¡Hasta luego!")