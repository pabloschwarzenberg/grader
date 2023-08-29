#Cajero Automático
def cajero_automatico():
    saldo_cajero = 1000000
    saldo_cuenta = 100000
    intentos = 0
    
    while True:
        usuario = input("Ingrese su usuario: ")
        clave = input("Ingrese su clave: ")
        
        if usuario == "10334151" and clave == "1803":
            print("Bienvenido, usuario.")
            break
        
        intentos += 1
        if intentos == 3:
            print("Tarjeta bloqueada. Contacte al banco.")
            return
        else:
            print("Clave inválida. Intente nuevamente.")
    
    while True:
        monto = float(input("Ingrese el monto a retirar: "))
        
        if monto <= 0:
            print("Monto no permitido. Intente nuevamente.")
        elif monto > saldo_cuenta:
            print("Saldo insuficiente. Intente nuevamente.")
        else:
            saldo_cuenta -= monto
            saldo_cajero -= monto
            print("Retiro exitoso.")
            print("Saldo cuenta =", saldo_cuenta)
            print("Saldo cajero =", saldo_cajero)
        
        opcion = input("¿Desea realizar otro retiro? (S/N): ")
        if opcion.upper() != "S":
            break

cajero_automatico()
