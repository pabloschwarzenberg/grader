def cajero():
    saldo_cuenta = 100000
    saldo_cajero = 1000000
    intentos_fallidos = 0
    
    while True:
        usuario = input("Ingrese su usuario: ")
        clave = input("Ingrese su clave: ")
        
        if usuario == "10334151" and clave == "1803":
            print("Inicio de sesión exitoso.")
            saldo_cuenta_inicial = 100000
            saldo_cuenta -= saldo_cuenta_inicial
            break
        else:
            intentos_fallidos += 1
            if intentos_fallidos == 3:
                print("Tarjeta bloqueada.")
                return
            
            print("Clave inválida. Intente nuevamente.")
    
    while True:
        monto_retiro = float(input("Ingrese el monto a retirar: "))
        
        if monto_retiro <= saldo_cuenta and monto_retiro <= saldo_cajero:
            saldo_cuenta -= monto_retiro
            saldo_cajero -= monto_retiro
            print(f"Retiro exitoso.\nSaldo cuenta: {saldo_cuenta}\nSaldo cajero: {saldo_cajero}")
        elif monto_retiro > saldo_cuenta:
            print("Monto no permitido. Saldo insuficiente en la cuenta.")
        else:
            print("Monto no permitido. Saldo insuficiente en el cajero.")
        
        opcion = input("¿Desea realizar otro retiro? (S/N): ")
        if opcion.upper() != "S":
            break

cajero()

      