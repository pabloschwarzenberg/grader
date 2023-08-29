#Cajero Automático
saldo_cuenta = 100000
saldo_cajero = 1000000

billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

intentos = 0

usuario_valido = 10334151
clave_valida = 1803

while intentos < 3:
    usuario = int(input("Ingrese su número de usuario: "))
    clave = int(input("Ingrese su clave: "))

    if usuario == usuario_valido and clave == clave_valida:
        monto_retiro = float(input("Ingrese el monto a retirar: "))

        if monto_retiro <= saldo_cuenta and monto_retiro <= saldo_cajero:
            if monto_retiro % 5000 != 0:
                print("Monto no permitido.")
            else:
                billetes_20000_entregados = 0
                billetes_10000_entregados = 0
                billetes_5000_entregados = 0

                while monto_retiro >= 20000 and billetes_20000 > 0:
                    monto_retiro -= 20000
                    saldo_cajero -= 20000
                    saldo_cuenta -= 20000
                    billetes_20000_entregados += 1
                    billetes_20000 -= 1

                while monto_retiro >= 10000 and billetes_10000 > 0:
                    monto_retiro -= 10000
                    saldo_cajero -= 10000
                    saldo_cuenta -= 10000
                    billetes_10000_entregados += 1
                    billetes_10000 -= 1

                while monto_retiro >= 5000 and billetes_5000 > 0:
                    monto_retiro -= 5000
                    saldo_cajero -= 5000
                    saldo_cuenta -= 5000
                    billetes_5000_entregados += 1
                    billetes_5000 -= 1

                print("Retiro exitoso.")
                print("Saldo cuenta =", saldo_cuenta)
                print("Saldo cajero =", saldo_cajero)
                print("Billetes 20000 =", billetes_20000_entregados)
                print("Billetes 10000 =", billetes_10000_entregados)
                print("Billetes 5000 =", billetes_5000_entregados)
        else:
            print("Monto no permitido.")
        
        break
    else:
        print("Clave inválida.")
        intentos += 1

if intentos == 3:
    print("Tarjeta bloqueada.")
     