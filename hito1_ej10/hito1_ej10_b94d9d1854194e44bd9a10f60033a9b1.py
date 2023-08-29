# Saldo inicial del cajero
saldo_cajero = 1000000

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
            # Actualizar saldos
            saldo_usuario -= monto
            saldo_cajero -= monto
            
            # Imprimir nuevos saldos
            print(f"Saldo cuenta: {saldo_usuario}")
            print(f"Saldo cajero: {saldo_cajero}")
            
            # Preguntar si se quiere realizar otra transacción
            continuar = input("¿Desea realizar otra transacción? (S/N): ")
            
            if continuar.upper() == "N":
                quit()
