#Cajero Automático
saldo_cajero = 1000000
saldo_cuenta = 100000
usuario = "10334151"
clave = "1803"
intentos = 0

while True:
    usuario_ingresado = input("Ingresa tu usuario: ")
    clave_ingresada = input("Ingresa tu clave: ")
    
    if usuario_ingresado == usuario and clave_ingresada == clave:
        monto = int(input("Ingresa el monto a retirar: "))
        if 0 < monto <= saldo_cuenta and monto <= saldo_cajero:
            saldo_cuenta -= monto
            saldo_cajero -= monto
            print("saldo cuenta =", saldo_cuenta)
            print("saldo cajero =", saldo_cajero)
        else:
            print("monto no permitido")
    else:
        print("clave invalida")
        intentos += 1
        if intentos == 3:
            # La tarjeta se bloquea
            print("tarjeta bloqueada")
            break
    continuar = input("¿Deseas continuar? (N para salir): ")
    if continuar != "N":
        break
