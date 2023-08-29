def cajero():
    saldo_cuenta = 100000
    saldo_cajero = 1000000
    intentos = 0
    
    while True:
        usuario = input("Ingrese su usuario: ")
        clave = input("Ingrese su clave: ")
        
        if usuario == "10334151" and clave == "1803":
            print("Acceso permitido")
            
            while True:
                monto = float(input("Ingrese el monto a retirar: "))
                
                if monto > saldo_cuenta:
                    print("Monto no permitido. Su saldo es insuficiente.")
                elif monto > saldo_cajero:
                    print("Monto no permitido. El cajero no tiene suficiente dinero.")
                else:
                    saldo_cuenta -= monto
                    saldo_cajero -= monto
                    print("Retiro exitoso")
                    print("Saldo cuenta:", saldo_cuenta)
                    print("Saldo cajero:", saldo_cajero)
                    break
        else:
            print("Clave inválida")
            intentos += 1
            
            if intentos == 3:
                print("Tarjeta bloqueada")
                break
        
        opcion = input("¿Desea realizar otra transacción? (S/N): ")
        
        if opcion.upper() != "S":
            break

# Ejecutar el programa
cajero()


      