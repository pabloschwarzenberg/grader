saldo_cuenta = 100000
saldo_cajero = 1000000
intentos = 0

usuario_valido = 10334151
clave_valida = 1803

saldo_total = 1000000
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

def retirar(saldo, monto, billetes_20000, billetes_10000, billetes_5000):
    if saldo < monto:
        print("No hay suficiente saldo en la cuenta.")
        return saldo, billetes_20000, billetes_10000, billetes_5000

    if monto % 5000 != 0:
        print("El monto debe ser múltiplo de 5000.")
        return saldo, billetes_20000, billetes_10000, billetes_5000
    
    billetes_20000_entregados = min(billetes_20000, monto // 20000)
    monto -= billetes_20000_entregados * 20000

    billetes_10000_entregados = min(billetes_10000, monto // 10000)
    monto -= billetes_10000_entregados * 10000

    billetes_5000_entregados = min(billetes_5000, monto // 5000)
    monto -= billetes_5000_entregados * 5000

    if monto != 0:
        print("No se pueden entregar los billetes exactos para el monto solicitado.")
        return saldo, billetes_20000, billetes_10000, billetes_5000

    billetes_20000 -= billetes_20000_entregados
    billetes_10000 -= billetes_10000_entregados
    billetes_5000 -= billetes_5000_entregados
    
    print("Saldo en cuenta:", saldo_cuenta - monto)
    print("Billetes entregados:")
    print("Billetes de 20000:", billetes_20000_entregados)
    print("Billetes de 10000:", billetes_10000_entregados)
    print("Billetes de 5000:", billetes_5000_entregados)
    
    return saldo - monto, billetes_20000, billetes_10000, billetes_5000

if __name__ == "__main__":
    while intentos < 3:
        usuario = int(input("Ingrese su número de usuario: "))
        clave = int(input("Ingrese su clave: "))

        if usuario == usuario_valido and clave == clave_valida:
            monto_retiro = int(input("Ingrese el monto a retirar: "))

            if monto_retiro <= saldo_cuenta and monto_retiro <= saldo_cajero:
               
                saldo_cajero -= monto_retiro
                print("Saldo en cajero:", saldo_cajero)
                saldo_cuenta, billetes_20000, billetes_10000, billetes_5000 = retirar(saldo_cuenta, monto_retiro, billetes_20000, billetes_10000, billetes_5000)
                break

            else:
                print("Monto no permitido.")
        else:
            print("Clave inválida.")
            intentos += 1

    if intentos==3:
        print("Tarjeta bloquada")


