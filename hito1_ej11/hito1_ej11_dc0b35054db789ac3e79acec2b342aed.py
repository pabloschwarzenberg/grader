#Cajero Automático
saldo_cuenta = 100000
saldo_cajero = 1000000
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40
intentos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")
    
    if usuario == "10334151" and clave == "1803":
        print("Bienvenido!")
        break
    else:
        intentos += 1
        if intentos == 3:
            print("Tarjeta bloqueada.")
            exit()
        else:
            print("Clave inválida. Intente de nuevo.")
            continue

while True:
    monto = float(input("Ingrese el monto a retirar: "))
    
    if monto > saldo_cuenta or monto > saldo_cajero or monto <= 0:
        print("Monto no permitido.")
        continue
    else:
        saldo_cuenta -= monto
        saldo_cajero -= monto
        
        billetes_20000_retirados = min(int(monto / 20000), billetes_20000)
        billetes_10000_retirados = min(int((monto - billetes_20000_retirados * 20000) / 10000), billetes_10000)
        billetes_5000_retirados = min(int((monto - billetes_20000_retirados * 20000 - billetes_10000_retirados * 10000) / 5000), billetes_5000)
        
        billetes_20000 -= billetes_20000_retirados
        billetes_10000 -= billetes_10000_retirados
        billetes_5000 -= billetes_5000_retirados
        
        print("Retiro exitoso.")
        print("Saldo cuenta =", saldo_cuenta)
        print("Saldo cajero =", saldo_cajero)
        
        if billetes_20000_retirados > 0:
            print("Billetes de $20.000 entregados:", billetes_20000_retirados)
            
        if billetes_10000_retirados > 0:
            print("Billetes de $10.000 entregados:", billetes_10000_retirados)
            
        if billetes_5000_retirados > 0:
            print("Billetes de $5.000 entregados:", billetes_5000_retirados)
        
    respuesta = input("¿Desea realizar otro retiro? (S/N): ")
    if respuesta.upper() == "N":
        break      