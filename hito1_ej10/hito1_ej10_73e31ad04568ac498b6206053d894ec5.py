saldo_cuenta = 100000
saldo_cajero = 1000000
intentos_fallidos = 0

while True:
    usuario = input("Ingrese el número de usuario: ")
    clave = input("Ingrese la clave: ")
    
    if usuario == "10334151" and clave == "1803":
        print("Inicio de sesión exitoso")
        saldo_actual = saldo_cuenta
        intentos_fallidos = 0
        
        while True:
            monto_retiro = float(input("Ingrese el monto a retirar: "))
            
            if monto_retiro <= saldo_actual:
                if monto_retiro > 0:
                    saldo_actual -= monto_retiro
                    saldo_cajero -= monto_retiro
                    print("Retiro exitoso")
                    print("Saldo cuenta =", saldo_actual)
                    print("Saldo cajero =", saldo_cajero)
                else:
                    print("Monto no permitido")
            else:
                print("Saldo insuficiente")
            
            continuar = input("¿Desea realizar otro retiro? (N para salir): ")
            if continuar != "N":
                break
        
    else:
        intentos_fallidos += 1
        print("Clave inválida")
        
        if intentos_fallidos == 3:
            print("Tarjeta bloqueada")
            break
