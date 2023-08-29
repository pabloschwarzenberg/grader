saldo_cajero = 1000000
saldo_usuario = 100000


max_intentos_fallidos = 3
intentos_fallidos = 0


usuario_permitido = 10334151
clave_permitida = 1803


while True:
   
    usuario = int(input("Ingrese su usuario: "))
    clave = int(input("Ingrese su clave: "))

    
    if usuario != usuario_permitido or clave != clave_permitida:
        print("Clave inválida")
        intentos_fallidos += 1

        if intentos_fallidos >= max_intentos_fallidos:
            print("Tarjeta bloqueada")
            break
    else:
        
        monto_retiro = float(input("Ingrese el monto a retirar: "))

        if monto_retiro <= 0 or monto_retiro > saldo_usuario:
            print("Monto no permitido")
        else:
            
            saldo_usuario -= monto_retiro
            saldo_cajero -= monto_retiro

            print("Saldo cuenta =", saldo_usuario)
            print("Saldo cajero =", saldo_cajero)
            break