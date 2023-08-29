#Cajero Automático
saldoInicial = 1010000
intentos = 1
usuario = ""
clave = ""


while intentos < 3:
    usuario = input("\n¿Usuario?: ")
    clave = input("¿Clave?: ")
    
    if usuario == "10334151" and clave == "1803":
        cuentaInicio = 100000
        montoRetirar = int(input("¿Monto a retirar?: "))
        while montoRetirar > cuentaInicio:
            print("Monto no permitido")
            montoRetirar = int(input("Vuelva a ingresar monto a retirar: "))           
            
            
        if montoRetirar <= cuentaInicio:
            cuentaInicio = cuentaInicio - montoRetirar
            saldoCajero = saldoInicial - cuentaInicio
            print("Saldo cuenta=", cuentaInicio, "saldo cajero=", saldoCajero)
            break
                
    else:
        print("\nclave invalida...")
    
    intentos += 1
    
    if intentos == 3:
        print("\nTarjeta bloqueada")
     