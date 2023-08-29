#Cajero Automático
      saldo_cuenta = 100000
saldo_cajero = {
    20000: 20,
    10000: 40,
    5000: 40
}

intentos_fallidos = 0

while intentos_fallidos < 3:
    usuario = input("Ingrese el número de usuario: ")
    clave = input("Ingrese la clave: ")
    
    if usuario == "10334151" and clave == "1803":
        while True:
            monto = float(input("Ingrese el monto a retirar: "))
            
            if monto <= saldo_cuenta:
                billetes_retirados = {}
                
                for denominacion, cantidad_disponible in saldo_cajero.items():
                    cantidad_billetes = min(monto // denominacion, cantidad_disponible)
                    billetes_retirados[denominacion] = cantidad_billetes
                    monto -= cantidad_billetes * denominacion
                    saldo_cajero[denominacion] -= cantidad_billetes
                    
                saldo_cuenta -= monto
                
                print("Retiro exitoso")
                print(f"Saldo cuenta: {saldo_cuenta}")
                print("Billetes entregados:")
                for denominacion, cantidad_billetes in billetes_retirados.items():
                    print(f"Billetes {denominacion}: {cantidad_billetes}")
                break
            else:
                print("Monto no permitido. Supera el saldo de la cuenta.")
    else:
        print("Clave inválida")
        intentos_fallidos += 1

    if intentos_fallidos == 3:
        print("Tarjeta bloqueada")
        break
