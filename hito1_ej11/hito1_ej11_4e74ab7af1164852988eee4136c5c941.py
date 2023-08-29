saldo_inicial = 1000000
saldo_cuenta = 100000
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40
intentos = 0

while intentos < 3:
    usuario = int(input("Ingrese su usuario: "))
    clave = int(input("Ingrese su clave: "))

    if usuario == 10334151 and clave == 1803:
        print("Clave correcta")
        opcion = "S"
        while opcion == "S":
            monto = int(input("Ingrese el monto a retirar: "))
            if monto <= saldo_cuenta:
                if monto % 5000 != 0:
                    print("Monto no permitido")
                else:
                    billetes_20000_entregados = min(billetes_20000, monto // 20000)
                    monto -= billetes_20000_entregados * 20000
                    billetes_10000_entregados = min(billetes_10000, monto // 10000)
                    monto -= billetes_10000_entregados * 10000
                    billetes_5000_entregados = min(billetes_5000, monto // 5000)
                    monto -= billetes_5000_entregados * 5000

                    saldo_cuenta -= (billetes_20000_entregados * 20000) + (billetes_10000_entregados * 10000) + (billetes_5000_entregados * 5000)
                    saldo_inicial -= (billetes_20000_entregados * 20000) + (billetes_10000_entregados * 10000) + (billetes_5000_entregados * 5000)
                    
                    print(f"Saldo cuenta = {saldo_cuenta}")
                    print(f"Saldo cajero = {saldo_inicial}")
                    print(f"Billetes de 20000 entregados = {billetes_20000_entregados}")
                    print(f"Billetes de 10000 entregados = {billetes_10000_entregados}")
                    print(f"Billetes de 5000 entregados = {billetes_5000_entregados}")
            else:
                print("Monto no permitido")
            opcion = input("¿Desea realizar otro retiro? (S/N): ")
            opcion = opcion.upper()
        break
    else:
        print("Clave inválida")
        intentos += 1

if intentos == 3:
    print("Tarjeta bloqueada")
