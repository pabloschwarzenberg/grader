
def cajero():
    saldo_cuenta = 100000
    saldo_cajero = 1000000
    intentos = 0
    
    while True:
        usuario = input("Ingrese su usuario: ")
        clave = input("Ingrese su clave: ")
        
        if usuario == "10334151" and clave == "1803":
            break
        else:
            intentos += 1
            print("Clave inválida.")
            
            if intentos == 3:
                print("Tarjeta bloqueada.")
                return
        
    while True:
        monto = int(input("Ingrese el monto a retirar: "))
        
        if monto > saldo_cuenta:
            print("Monto no permitido.")
        else:
            saldo_cuenta -= monto
            saldo_cajero -= monto
            print("Saldo cuenta=",saldo_cuenta,"saldo cajero=", saldo_cajero)
            break
        
        opcion = input("¿Desea realizar otro retiro? (S/N): ")
        if opcion.upper() != "S":
            break

cajero()
