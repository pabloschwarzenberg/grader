#Cajero Automático
saldo_cuenta = 100000
saldo_cajero = 1000000
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40
intentos_fallidos = 0

usuario_valido = 10334151
clave_valida = 1803

while True:
    usuario = int(input("Ingrese su número de usuario: "))
    clave = int(input("Ingrese su clave: "))

    if usuario == usuario_valido and clave == clave_valida:
        print("Acceso permitido")
        break
    else:
        print("Clave inválida")
        intentos_fallidos += 1

    if intentos_fallidos == 3:
        print("Tarjeta bloqueada")
        exit()

while True:
    monto_retiro = float(input("Ingrese el monto a retirar: "))

    if monto_retiro <= saldo_cuenta and monto_retiro % 1000 == 0:
        saldo_cuenta -= monto_retiro
        saldo_cajero -= monto_retiro
        billetes_entregados = {
            20000: 0,
            10000: 0,
            5000: 0
        }

        while monto_retiro > 0:
            if monto_retiro >= 20000 and billetes_20000 > 0:
                billetes_entregados[20000] += 1
                monto_retiro -= 20000
                billetes_20000 -= 1
            elif monto_retiro >= 10000 and billetes_10000 > 0:
                billetes_entregados[10000] += 1
                monto_retiro -= 10000
                billetes_10000 -= 1
            elif monto_retiro >= 5000 and billetes_5000 > 0:
                billetes_entregados[5000] += 1
                monto_retiro -= 5000
                billetes_5000 -= 1
            else:
                break

        print("Retiro exitoso")
        print("Saldo cuenta =", saldo_cuenta)
        print("Saldo cajero =", saldo_cajero)
        for billete, cantidad in billetes_entregados.items():
            if cantidad > 0:
                print("Billetes", billete, "=", cantidad)
        break
    else:
        print("Monto no permitido")
           