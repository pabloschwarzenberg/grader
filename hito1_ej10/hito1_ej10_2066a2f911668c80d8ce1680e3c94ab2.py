#Cajero Automático
      
saldo_inicial_cajero = 1000000
cuenta_usuario = 100000 
intentos = 3
    

while intentos > 0:
    usuario = int(input("Ingrese usuario: "))
    clave = int(input("Ingrese Clave: "))
    
    if clave != 1803:
        intentos -= 1
        print(f"Clave invalida te quedan{intentos}intentos.")
    elif intentos == 0:
        print("Tarjeta Bloqueada") 
        break
           
            
    else:
        print("Clave valida, indique monto a retirar")
        
        monto_retirar = int(input("Monto a retirar: "))   
        
        if monto_retirar > 1000000: 
            print("Monto no permitido")
        else:
            saldo_cuenta = cuenta_usuario - monto_retirar
            saldo_cajero = saldo_inicial_cajero - monto_retirar
            print(f"saldo cuenta={saldo_cuenta}")
            print(f"saldo cajero={saldo_cajero}")
            
    opcion_salida = input("¿Desea realizar otra operación? (N para salir): ")
    if opcion_salida == "N":
        continuar = False