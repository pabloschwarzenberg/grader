saldo_cuenta = 100000
saldo_cajero = 1000000
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40
intentos = 0
usuario = 10334151
clave = 1803

while True:
    usuario_ingresado = int(input("Ingrese su usuario: "))
    clave_ingresada = int(input("Ingrese su clave: "))
    
    if usuario_ingresado == usuario and clave_ingresada == clave:
        print("Bienvenido!")
        break
    else:
        intentos += 1
        if intentos == 3:
            print("Tarjeta bloqueada.")
            exit()
        else:
            print("Clave invalida. Intente nuevamente.")
            continue

while True:
    monto_retiro = int(input("Ingrese el monto a retirar: "))
    if monto_retiro % 5000 != 0 or monto_retiro > saldo_cuenta or monto_retiro > saldo_cajero:
        print("Monto no permitido.")
        continue
    else:
        billetes_20000_retiro = min(billetes_20000, monto_retiro // 20000)
        monto_retiro -= billetes_20000_retiro * 20000
        billetes_10000_retiro = min(billetes_10000, monto_retiro // 10000)
        monto_retiro -= billetes_10000_retiro * 10000
        billetes_5000_retiro = min(billetes_5000, monto_retiro // 5000)
        monto_retiro -= billetes_5000_retiro * 5000
        
        saldo_cuenta -= (billetes_20000_retiro + billetes_10000_retiro + billetes_5000_retiro) * 5000
        saldo_cajero -= (billetes_20000_retiro * 20000 + billetes_10000_retiro * 10000 + billetes_5000_retiro * 5000)
        billetes_20000 -= billetes_20000_retiro
        billetes_10000 -= billetes_10000_retiro
        billetes_5000 -= billetes_5000_retiro
        
        print("Retiro exitoso. Saldo en cuenta:", saldo_cuenta, "Saldo en cajero:", saldo_cajero)
        print("Billetes entregados:")
        print("Billetes de 20000:", billetes_20000_retiro)
        print("Billetes de 10000:", billetes_10000_retiro)
        print("Billetes de 5000:", billetes_5000_retiro)
        
    seguir = input("Desea realizar otro retiro? (N para salir)").upper()
    if seguir == "N":
        break

print("Gracias por utilizar nuestro cajero automático!")
      