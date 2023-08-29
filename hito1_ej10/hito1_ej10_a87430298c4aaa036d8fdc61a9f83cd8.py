saldo_inicial = 1000000
saldo_cajero = 1000000
intentos = 0
usuario_valido = False

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")
    
    if usuario == "10334151" and clave == "1803":
        saldo_usuario = 100000
        usuario_valido = True
    else:
        intentos += 1
        print("Clave inválida.")
        if intentos == 3:
            print("Tarjeta bloqueada.")
            break  # Salir del bucle y finalizar el programa
    
    if usuario_valido:
        monto = int(input("Ingrese el monto a retirar: "))
        
        if monto <= 0:
            print("Monto no permitido.")
        elif monto > saldo_usuario or monto > saldo_cajero:
            print("Monto no permitido.")
        else:
            saldo_usuario -= monto
            saldo_cajero -= monto
            print("Saldo cuenta =", saldo_usuario)
            print("Saldo cajero =", saldo_cajero)
            
    opcion = input("¿Desea realizar otro retiro? (N para salir): ")
    if opcion.upper() != "N":
        break  # Salir del bucle y finalizar el programa
