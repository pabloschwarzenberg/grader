def cajero():
    # Saldo inicial del cajero y el usuario
    saldo_cajero = {
        20000: 20,
        10000: 40,
        5000: 40
    }
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
            intentos_clave += 1
            if intentos_clave == 3:
                print("Tarjeta bloqueada")
                return
    
    while True:
        monto_retiro = int(input("Ingrese el monto a retirar: "))
        
        # Verificar si el monto es válido
        if monto_retiro <= saldo_usuario and monto_retiro <= sum(k * v for k, v in saldo_cajero.items()):
            # Realizar el retiro y actualizar saldos
            saldo_usuario -= monto_retiro
            saldo_cajero_actualizado = saldo_cajero.copy()
            
            # Distribuir el monto en billetes
            billetes_entregados = {}
            for billete, cantidad in sorted(saldo_cajero_actualizado.items(), reverse=True):
                cantidad_entregada = min(monto_retiro // billete, cantidad)
                monto_retiro -= billete * cantidad_entregada
                saldo_cajero_actualizado[billete] -= cantidad_entregada
                if cantidad_entregada > 0:
                    billetes_entregados[billete] = cantidad_entregada
            
            # Imprimir saldos y billetes entregados
            print("Saldo cuenta =", saldo_usuario)
            print("Saldo cajero =", sum(k * v for k, v in saldo_cajero_actualizado.items()))
            for billete, cantidad_entregada in billetes_entregados.items():
                print("billetes", billete, "=", cantidad_entregada)
        else:
            print("Monto no permitido")
        
        opcion = input("¿Desea realizar otro retiro? (S/N): ")
        if opcion.upper() != "S":
            break

cajero()
