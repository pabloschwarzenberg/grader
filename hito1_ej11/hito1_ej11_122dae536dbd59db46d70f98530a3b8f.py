#Cajero Automático
 saldo_inicial = 1000000
saldo_usuario = 100000
intentos_fallidos = 0

billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

def pedir_clave():
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        return True
    else:
        return False

def calcular_billetes(monto):
    billetes_20000_retirados = min(monto // 20000, billetes_20000)
    monto -= billetes_20000_retirados * 20000

    billetes_10000_retirados = min(monto // 10000, billetes_10000)
    monto -= billetes_10000_retirados * 10000

    billetes_5000_retirados = min(monto // 5000, billetes_5000)
    monto -= billetes_5000_retirados * 5000

    return (billetes_20000_retirados, billetes_10000_retirados, billetes_5000_retirados)

while intentos_fallidos < 3:
    if pedir_clave():
        while True:
            monto_retiro = int(input("Ingrese el monto a retirar: "))

            if monto_retiro <= saldo_usuario:
                if monto_retiro <= saldo_inicial:
                    billetes_20000_retirados, billetes_10000_retirados, billetes_5000_retirados = calcular_billetes(monto_retiro)

                    saldo_usuario -= monto_retiro
                    saldo_inicial -= monto_retiro

                    print("Retiro exitoso.")
                    print("Nuevo saldo en la cuenta corriente:", saldo_usuario)
                    print("Nuevo saldo en el cajero:", saldo_inicial)
                    print("Billetes entregados:")
                    print("Billetes de 20.000:", billetes_20000_retirados)
                    print("Billetes de 10.000:", billetes_10000_retirados)
                    print("Billetes de 5.000:", billetes_5000_retirados)

                    break
                else:
                    print("El cajero no tiene suficiente saldo para realizar el retiro.")
            else:
                print("Monto no permitido.")
    else:
        intentos_fallidos += 1
        if intentos_fallidos < 3:
            print("Clave inválida. Intenta nuevamente.")
        else:
            print("Tarjeta bloqueada.")     