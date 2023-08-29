#Cajero Automático
saldo_inicial = 1000000
saldo_usuario = 100000
intentos = 0

usuario_valido = 10334151
clave_valida = 1803

usuario = int(input("Ingrese su número de usuario: "))
clave = int(input("Ingrese su clave: "))
if usuario == usuario_valido and clave == clave_valida:
    print("Acceso permitido")    
    monto = float(input("Ingrese el monto a retirar: "))    
    
    if monto > saldo_usuario:
        print("Monto no permitido")
    else:
      
        saldo_usuario -= monto
        saldo_inicial -= monto
        print("Retiro exitoso")
        round_usuario = round(saldo_usuario)
        round_inicial = round(saldo_inicial)
        print("saldo cuenta=", round_usuario)
        print("saldo cajero=", round_inicial)
else:
    print("Clave inválida")
    intentos += 1

    if intentos == 3:
        print("Tarjeta bloqueada")     