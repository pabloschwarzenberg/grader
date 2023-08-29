def cajero():
    # Saldo inicial del cajero y el usuario
    saldo_cajero = 1000000
    saldo_usuario = 100000
    
    # Variables para controlar el ingreso de usuario y clave
    usuario_valido = False
    clave_valida = False
    
    # Contadores de intentos de clave incorrecta
    intentos_clave = 0
    
    # Datos de usuario y clave válidos
    usuario_valido = "10334151"
    clave_valida = "1803"
    
    while True:
        # Ingreso de usuario y clave
        usuario_ingresado = input("Ingrese su usuario: ")
        clave_ingresada = input("Ingrese su clave: ")
        
        # Validación de usuario y clave
        if usuario_ingresado == usuario_valido and clave_ingresada == clave_valida:
            print("Acceso permitido")
            break
        else:
            print("Usuario o clave incorrectos")
            intentos_clave += 1
            
        # Verificar si se superó el límite de intentos de clave incorrecta
        if intentos_clave == 3:
            print("Tarjeta bloqueada")
            return
        
    # Bucle principal para retirar dinero
    while True:
        monto_retiro = float(input("Ingrese el monto a retirar: "))
        
        # Validación del monto a retirar
        if monto_retiro <= saldo_usuario and monto_retiro <= saldo_cajero:
            saldo_usuario -= monto_retiro
            saldo_cajero -= monto_retiro
            print("Retiro exitoso")
            print("Saldo cuenta = {}".format(saldo_usuario))
            print("Saldo cajero = {}".format(saldo_cajero))
        else:
            print("Monto no permitido")
        
        opcion = input("¿Desea realizar otro retiro? (S/N): ")
        if opcion.upper() != "S":
            break

# Ejecutar el programa del cajero automático
cajero()
