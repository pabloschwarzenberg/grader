#Cajero Automático
saldo_cuenta = 100000
saldo_cajero = 1000000

intentos = 0
usuario_valido = False
clave_valida = False

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")
    
    if usuario == "10334151" and clave == "1803":
        usuario_valido = True
        break
    
    intentos += 1
    if intentos == 3:
        print("Tarjeta bloqueada. Ha excedido el número de intentos.")
        exit()
    else:
        print("Clave inválida. Por favor, intente nuevamente.")

while True:
    monto = float(input("Ingrese el monto a retirar: "))
    
    if monto > saldo_cuenta:
        print("Monto no permitido. No tiene suficiente saldo en su cuenta.")
    elif monto > saldo_cajero:
        print("Monto no permitido. El cajero no dispone de suficiente efectivo.")
    else:
        saldo_cuenta -= monto
        saldo_cajero -= monto
        print("Retiro exitoso.")
        print("Saldo cuenta =", saldo_cuenta)
        print("Saldo cajero =", saldo_cajero)
    
    opcion = input("¿Desea realizar otra transacción? (S/N): ")
    if opcion.upper() != "S":
        break