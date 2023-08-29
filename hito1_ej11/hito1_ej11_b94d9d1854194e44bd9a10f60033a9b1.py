#Cajero Automático
# Saldo inicial del cajero
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

# Saldo inicial del usuario
saldo_usuario = 100000
clave_correcta = False
intentos = 0

while True:
    # Pedir usuario y clave
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")
    
    # Validar usuario y clave
    if usuario == "10334151" and clave == "1803":
        clave_correcta = True
        break
    else:
        print("Clave inválida")
        intentos += 1
        
    # Si se ingresaron tres claves incorrectas, se bloquea la tarjeta
    if intentos == 3:
        print("Tarjeta bloqueada")
        quit()

# Si la clave es correcta, permitir retirar dinero
if clave_correcta:
    while True:
        # Pedir monto a retirar
        monto = float(input("Ingrese el monto a retirar: "))
        
        # Validar el monto
        if monto <= 0:
            print("Monto no permitido")
        elif monto > saldo_usuario:
            print("No cuenta con suficiente saldo para realizar esta operación")
        else:
            # Calcular la cantidad de billetes de cada denominación a entregar
            billetes_20000_entregados = min(monto // 20000, billetes_20000)
            monto -= billetes_20000_entregados * 20000
            billetes_10000_entregados = min(monto // 10000, billetes_10000)
            monto -= billetes_10000_entregados * 10000
            billetes_5000_entregados = min(monto // 5000, billetes_5000)
            monto -= billetes_5000_entregados * 5000
            
            # Actualizar saldos
            saldo_usuario -= (billetes_20000_entregados * 20000 +
                              billetes_10000_entregados * 10000 +
                              billetes_5000_entregados * 5000)
            billetes_20000 -= billetes_20000_entregados
            billetes_10000 -= billetes_10000_entregados
            billetes_5000 -= billetes_5000_entregados
            
            # Imprimir nuevos saldos
            print(f"Saldo cuenta: {saldo_usuario}")
            print(f"Saldo cajero - Billetes de 20000: {billetes_20000}")
            print(f"Saldo cajero - Billetes de 10000: {billetes_10000}")
            print(f"Saldo cajero - Billetes de 5000: {billetes_5000}")
            
            # Imprimir cantidad de billetes entregados
            print(f"Billetes de 20000: {billetes_20000_entregados}")
            print(f"Billetes de 10000: {billetes_10000_entregados}")
            print(f"Billetes de 5000: {billetes_5000_entregados}")
            
            # Preguntar si se quiere realizar otra transacción
            continuar = input("¿Desea realizar otra transacción? (S/N): ")
            
            if continuar.upper() == "N":
                quit()
      