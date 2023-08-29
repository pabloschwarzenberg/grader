saldo_cajero = 1000000
saldo_usuario = 100000

intentos_fallidos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        intentos_fallidos = 0

        
        monto = int(input("Ingrese el monto a retirar: "))

        if monto > saldo_usuario or monto > saldo_cajero:
            print("Monto no permitido")
        else:
            
            saldo_usuario -= monto
            saldo_cajero -= monto

            
            print("saldo cuenta=" + str(saldo_usuario))
            print("saldo cajero=" + str(saldo_cajero))
    else:
        
        intentos_fallidos += 1

        
        if intentos_fallidos == 3:
            print("Tarjeta bloqueada")
            break
        else:
            print("Clave invalida")

    
    continuar = input("¿Desea continuar? (N para salir): ")
    if continuar != "N":
        break
