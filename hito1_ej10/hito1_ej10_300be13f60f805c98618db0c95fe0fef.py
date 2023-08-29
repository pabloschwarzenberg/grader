def cajero():
    saldo_cuenta = 100000
    saldo_cajero = 1000000
    intentos_fallidos = 0
    
    while True:
        usuario = input("Ingrese su usuario: ")
        clave = input("Ingrese su clave: ")
        
        if usuario == "10334151" and clave == "1803":
            print("¡Bienvenido!")
            break
        else:
            intentos_fallidos += 1
            print("Clave inválida")
            
        if intentos_fallidos >= 3:
            print("Tarjeta bloqueada")
            return
    
    while True:
        try:
            monto = float(input("Ingrese el monto a retirar: "))
            
            if monto <= 0:
                print("Monto no permitido")
            elif monto > saldo_cuenta or monto > saldo_cajero:
                print("Saldo insuficiente en la cuenta o en el cajero")
            else:
                saldo_cuenta -= monto
                saldo_cajero -= monto
                print("Retiro exitoso")
                print(["saldo cuenta=" + str(saldo_cuenta), "saldo cajero=" + str(saldo_cajero)])
                
                respuesta = input("¿Desea realizar otro retiro? (S/N): ")
                
                if respuesta.upper() != "S":
                    break
        except ValueError:
            print("Monto inválido")
        

cajero()
