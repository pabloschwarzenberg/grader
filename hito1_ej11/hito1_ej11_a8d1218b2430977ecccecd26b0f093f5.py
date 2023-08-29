#Cajero Automático
usuario = "10334151"
clave = "1803"
saldo_cuenta = 100000
saldo_cajero = 1000000
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

print("- Tecla N para retirar\n- Cualquier otra tecla para salir.")

intentos = 0
bloqueado = False

while True:
    opcion = input("Seleccione opción: ")
    
    if opcion.upper() != "N":
        break
    
    iu = input("Indique usuario: ")
    
    if iu != usuario:
        print("Usuario inválido")
        continue
    
    ic = input("Indique clave: ")
    
    if ic != clave:
        intentos += 1
        print("Clave inválida")
        
        if intentos >= 3:
            bloqueado = True
            print("Tarjeta bloqueada")
            break
    else:
        monto = int(input("Ingrese monto a retirar de la cuenta: "))
        
        if monto <= 0:
            print("Monto no permitido")
            continue
        
        if monto > saldo_cuenta:
            print("Saldo insuficiente")
            continue
        
        # Distribuir el monto en los billetes disponibles
        billetes_20000_retirados = monto // 20000
        if billetes_20000_retirados > billetes_20000:
            billetes_20000_retirados = billetes_20000
        monto -= billetes_20000_retirados * 20000
        
        billetes_10000_retirados = monto // 10000
        if billetes_10000_retirados > billetes_10000:
            billetes_10000_retirados = billetes_10000
        monto -= billetes_10000_retirados * 10000
        
        billetes_5000_retirados = monto // 5000
        if billetes_5000_retirados > billetes_5000:
            billetes_5000_retirados = billetes_5000
        monto -= billetes_5000_retirados * 5000
        
        saldo_cuenta -= (billetes_20000_retirados * 20000) + (billetes_10000_retirados * 10000) + (billetes_5000_retirados * 5000)
        saldo_cajero -= (billetes_20000_retirados * 20000) + (billetes_10000_retirados * 10000) + (billetes_5000_retirados * 5000)
        
        print(f"Saldo cuenta = {saldo_cuenta}")
        print(f"Saldo cajero = {saldo_cajero}")
        print(f"Billetes 20000 = {billetes_20000_retirados}")
        print(f"Billetes 10000 = {billetes_10000_retirados}")
        print(f"Billetes 5000 = {billetes_5000_retirados}")

    print("- Tecla N para retirar\n- Cualquier otra tecla para salir.")
 