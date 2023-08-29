#Cajero Automático
def cajero():
    usuario_valido = 10334151
    clave_valida = 1803
    intentos_fallidos = 0
    saldo_cuenta = 100000
    saldo_cajero = 1000000
    
    while True:
        usuario = int(input("Ingrese su usuario: "))
        clave = int(input("Ingrese su clave: "))
        
        if usuario == usuario_valido and clave == clave_valida:
            print("Inicio de sesión exitoso.")
            break
        else:
            intentos_fallidos += 1
            if intentos_fallidos == 3:
                print("Tarjeta bloqueada. Demasiados intentos fallidos.")
                return
        
            print("Clave inválida. Por favor, intente nuevamente.")

    while True:
        try:
            monto = float(input("Ingrese el monto a retirar: "))
        except ValueError:
            print("Error: Por favor, ingrese un monto válido.")
            continue
        
        if monto <= saldo_cuenta and monto <= saldo_cajero:
            saldo_cuenta -= monto
            saldo_cajero -= monto
            print("Retiro exitoso.")
            print("Saldo cuenta:", saldo_cuenta)
            print("Saldo cajero:", saldo_cajero)
        elif monto > saldo_cuenta:
            print("Monto no permitido. Saldo insuficiente en la cuenta.")
        elif monto > saldo_cajero:
            print("Monto no permitido. Saldo insuficiente en el cajero.")
        
        opcion = input("¿Desea realizar otro retiro? (N para salir): ")
        if opcion.lower() == "n":
            break

cajero()


      