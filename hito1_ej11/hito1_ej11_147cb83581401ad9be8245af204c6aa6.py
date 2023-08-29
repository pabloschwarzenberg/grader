saldo_inicial_cajero = {
    20000: 20,
    10000: 40,
    5000: 40
}

saldo_inicial_cuenta = 100000
intentos_fallidos = 0

def verificar_clave(usuario, clave):
    if usuario == 10334151 and clave == 1803:
        return True
    else:
        return False

def retirar_dinero(monto):
    global saldo_inicial_cuenta, saldo_inicial_cajero
    billetes_entregados = {}
    monto_restante = monto

    if monto <= saldo_inicial_cuenta:
        if monto <= sum(saldo_inicial_cajero.keys()):
            for denominacion, cantidad in sorted(saldo_inicial_cajero.items(), reverse=True):
                if monto_restante >= denominacion and cantidad > 0:
                    billetes = min(monto_restante // denominacion, cantidad)
                    monto_restante -= denominacion * billetes
                    saldo_inicial_cajero[denominacion] -= billetes
                    billetes_entregados[denominacion] = billetes

            if monto_restante == 0:
                saldo_inicial_cuenta -= monto
                print("Retiro exitoso.")
                print("Nuevo saldo en la cuenta:", saldo_inicial_cuenta)
                print("Nuevo saldo en el cajero:", saldo_inicial_cajero)
                print("Billetes entregados:")
                for denominacion, cantidad in billetes_entregados.items():
                    print("billetes", denominacion, "=", cantidad)
            else:
                print("Monto no permitido. No hay suficientes billetes para completar el retiro.")
        else:
            print("Monto no permitido. Saldo insuficiente en el cajero.")
    else:
        print("Monto no permitido. Saldo insuficiente en la cuenta.")

while intentos_fallidos < 3:
    usuario = int(input("Ingrese su número de usuario: "))
    clave = int(input("Ingrese su clave: "))

    if verificar_clave(usuario, clave):
        monto_retiro = float(input("Ingrese el monto a retirar: "))
        retirar_dinero(monto_retiro)
        break
    else:
        print("Clave inválida.")
        intentos_fallidos += 1

if intentos_fallidos == 3:
    print("Tarjeta bloqueada. Por favor, contacte al banco.")
