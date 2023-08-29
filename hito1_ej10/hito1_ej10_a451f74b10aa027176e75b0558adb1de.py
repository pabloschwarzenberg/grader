saldo_cuenta = 100000
saldo_cajero = 1000000
intentos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")
    
    if usuario == "10334151" and clave == "1803":
        print("Bienvenido, tiene un saldo inicial de", saldo_cuenta)
        break
    else:
        intentos += 1
        if intentos == 3:
            print("Tarjeta bloqueada.")
            break
        else:
            print("Clave inválida. Intentos restantes:", 3-intentos)

while True:
    monto = float(input("Ingrese el monto a retirar: "))
    
    if monto > saldo_cuenta or monto % 10000 != 0:
        print("Monto no permitido.")
    else:
        saldo_cuenta -= monto
        saldo_cajero -= monto
        print("Saldo cuenta:", saldo_cuenta)
        print("Saldo cajero:", saldo_cajero)
        
    respuesta = input("¿Desea realizar otro retiro? (S/N)")
    if respuesta.upper() == "N":
        break
