#Cajero Automático
def cajero():
    usuario_valido = 10334151
    clave_valida = 1803
    intentos_fallidos = 0
    saldo_cuenta = 100000
    saldo_cajero = {
        20000: 20,
        10000: 40,
        5000: 40
    }
    
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
        
        if monto <= saldo_cuenta and monto <= sum([billete * cantidad for billete, cantidad in saldo_cajero.items()]):
            billetes_entregados = {}
            for billete, cantidad in sorted(saldo_cajero.items(), reverse=True):
                if monto >= billete and cantidad > 0:
                    cant_billetes = min(monto // billete, cantidad)
                    monto -= billete * cant_billetes
                    saldo_cajero[billete] -= cant_billetes
                    billetes_entregados[billete] = cant_billetes
            
            saldo_cuenta -= monto
            print("Retiro exitoso.")
            print("Saldo cuenta:", saldo_cuenta)
            print("Saldo cajero:", saldo_cajero)
            print("Billetes entregados:")
            for billete, cantidad in billetes_entregados.items():
                print(f"Billetes {billete} = {cantidad}")
        elif monto > saldo_cuenta:
            print("Monto no permitido. Saldo insuficiente en la cuenta.")
        elif monto > sum([billete * cantidad for billete, cantidad in saldo_cajero.items()]):
            print("Monto no permitido. Saldo insuficiente en el cajero.")
        
        opcion = input("¿Desea realizar otro retiro? (N para salir): ")
        if opcion.lower() == "n":
            break

cajero()
      