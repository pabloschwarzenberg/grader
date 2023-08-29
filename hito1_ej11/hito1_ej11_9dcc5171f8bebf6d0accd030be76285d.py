saldo_cuenta = 100000
saldo_cajero = 1000000
intentos = 0
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")
    
    if usuario == "10334151" and clave == "1803":
        break
    else:
        intentos += 1
        if intentos == 3:
            print("Tarjeta bloqueada")
            exit()
        else:
            print("Clave inválida. Intente nuevamente.")

while True:
    try:
        monto = float(input("Ingrese el monto a retirar: "))
        break
    except ValueError:
        print("Monto no válido. Intente nuevamente.")

if monto > saldo_cuenta:
    print("Monto no permitido. Saldo insuficiente.")
else:
    if monto > saldo_cajero:
        print("Monto no permitido. Cajero sin suficiente efectivo.")
    else:
        # Distribución de billetes
        billetes_entregados = {
            "billetes 20000": 0,
            "billetes 10000": 0,
            "billetes 5000": 0
        }
        
        total_entregado = 0
        
        while monto > 0:
            if monto >= 20000 and billetes_20000 > 0:
    cantidad_billetes = min(monto // 20000, billetes_20000)
    monto -= cantidad_billetes * 20000
    saldo_cajero -= cantidad_billetes * 20000
    billetes_20000 -= cantidad_billetes
    billetes_entregados["billetes_20000"] += cantidad_billetes
    total_entregado += cantidad_billetes * 20000
elif monto >= 10000 and billetes_10000 > 0:
    cantidad_billetes = min(monto // 10000, billetes_10000)
    monto -= cantidad_billetes * 10000
    saldo_cajero -= cantidad_billetes * 10000
    billetes_10000 -= cantidad_billetes
    billetes_entregados["billetes_10000"] += cantidad_billetes
    total_entregado += cantidad_billetes * 10000
elif monto >= 5000 and billetes_5000 > 0:
    cantidad_billetes = min(monto // 5000, billetes_5000)
    monto -= cantidad_billetes * 5000
    saldo_cajero -= cantidad_billetes * 5000
    billetes_5000 -= cantidad_billetes
    billetes_entregados["billetes_5000"] += cantidad_billetes
    total_entregado += cantidad_billetes * 5000

            else:
                break
     
        saldo_cuenta -= total_entregado
        
        print("Saldo cuenta={}".format(saldo_cuenta))
        print("Saldo cajero={}".format(saldo_cajero))
        
        for billete, cantidad in billetes_entregados.items():
            print("{} = {}".format(billete, cantidad))
