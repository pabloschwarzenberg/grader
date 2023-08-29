#Cajero Automático
saldo_cuenta = 100000
saldo_cajero = 1000000
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40
intentos_fallidos = 0

# Validar usuario y clave
usuario = input("Ingrese su usuario: ")
clave = input("Ingrese su clave: ")

if usuario == "10334151" and clave == "1803":
    while intentos_fallidos < 3:
        monto_retiro = float(input("Ingrese el monto a retirar: "))

        # Validar monto a retirar
        if monto_retiro <= 0:
            print("Monto no permitido.")
        elif monto_retiro > saldo_cuenta:
            print("Saldo insuficiente.")
        else:
            # Calcular cantidad de billetes
            billetes_20000_retiro = min(int(monto_retiro / 20000), billetes_20000)
            monto_retiro -= billetes_20000_retiro * 20000

            billetes_10000_retiro = min(int(monto_retiro / 10000), billetes_10000)
            monto_retiro -= billetes_10000_retiro * 10000

            billetes_5000_retiro = min(int(monto_retiro / 5000), billetes_5000)
            monto_retiro -= billetes_5000_retiro * 5000

            # Actualizar saldos y cantidad de billetes
            saldo_cuenta -= (billetes_20000_retiro * 20000) + (billetes_10000_retiro * 10000) + (billetes_5000_retiro * 5000)
            saldo_cajero -= (billetes_20000_retiro * 20000) + (billetes_10000_retiro * 10000) + (billetes_5000_retiro * 5000)
            billetes_20000 -= billetes_20000_retiro
            billetes_10000 -= billetes_10000_retiro
            billetes_5000 -= billetes_5000_retiro

            # Imprimir resultados
            print("Retiro exitoso.")
            print("Saldo cuenta =", saldo_cuenta)
            print("Saldo cajero =", saldo_cajero)
            print("Billetes 20000 =", billetes_20000_retiro)
            print("Billetes 10000 =", billetes_10000_retiro)
            print("Billetes 5000 =", billetes_5000_retiro)

            break
else:
    print("Usuario o clave inválida.")
    intentos_fallidos += 1

if intentos_fallidos == 3:
    print("Tarjeta bloqueada.")
      