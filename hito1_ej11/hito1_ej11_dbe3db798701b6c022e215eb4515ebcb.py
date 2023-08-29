#Cajero Automático
saldo_cuenta = 100000
saldo_cajero = 1000000
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40
intentos_fallidos = 0

resultado = []

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        resultado.append("Inicio de sesión exitoso.")
        break
    else:
        resultado.append("Usuario o clave incorrectos.")
        intentos_fallidos += 1

        if intentos_fallidos == 3:
            resultado.append("Tarjeta bloqueada. Contacte al banco.")
            break

while True:
    monto_retiro = float(input("Ingrese el monto a retirar: "))

    if monto_retiro > saldo_cuenta or monto_retiro > saldo_cajero:
        resultado.append("Monto no permitido. Verifique su saldo.")
    else:
        # Verificar disponibilidad de billetes
        if monto_retiro % 5000 != 0 or monto_retiro > (billetes_20000 * 20000) + (billetes_10000 * 10000) + (billetes_5000 * 5000):
            resultado.append("No es posible entregar el monto solicitado.")
        else:
            # Calcular cantidad de billetes
            billetes_20000_retiro = min(monto_retiro // 20000, billetes_20000)
            monto_retiro -= billetes_20000_retiro * 20000

            billetes_10000_retiro = min(monto_retiro // 10000, billetes_10000)
            monto_retiro -= billetes_10000_retiro * 10000

            billetes_5000_retiro = min(monto_retiro // 5000, billetes_5000)

            # Actualizar saldos y cantidad de billetes
            saldo_cuenta -= (billetes_20000_retiro * 20000) + (billetes_10000_retiro * 10000) + (billetes_5000_retiro * 5000)
            saldo_cajero -= (billetes_20000_retiro * 20000) + (billetes_10000_retiro * 10000) + (billetes_5000_retiro * 5000)
            billetes_20000 -= billetes_20000_retiro
            billetes_10000 -= billetes_10000_retiro
            billetes_5000 -= billetes_5000_retiro

            resultado.append("Retiro exitoso.")
            resultado.append("Saldo cuenta: " + str(saldo_cuenta))
            resultado.append("Saldo cajero: " + str(saldo_cajero))
            resultado.append("Billetes 20000: " + str(billetes_20000_retiro))
            resultado.append("Billetes 10000: " + str(billetes_10000_retiro))
            resultado.append("Billetes 5000: " + str(billetes_5000_retiro))

    opcion = input("¿Desea realizar otro retiro? (S/N): ")
    if opcion != "S":
        break

print(resultado)    