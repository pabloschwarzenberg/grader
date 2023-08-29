#Cajero Automático
saldo_cuenta = 100000
saldo_cajero = 1000000
intentos = 0

while True:
    usuario = input("Ingrese usuario: ")
    clave = input("Ingrese clave: ")
    
    if usuario == '10334151' and clave == '1803':
        while True:
            monto = input("Ingrese monto a retirar: ")
            try:
                monto = int(monto)
            except ValueError:
                break # Salir si no ingresó un número

            if monto % 10000 != 0 or monto < 10000 or monto > saldo_cuenta:
                print("Monto no permitido")
            else:
                saldo_cuenta -= monto
                saldo_cajero += monto
                print("Saldo cuenta = ", saldo_cuenta)
                print("Saldo cajero = ", saldo_cajero)

        intentos = 0 # Reiniciar intentos fallidos cuando sale del bucle de retiros
    else:
        intentos += 1
        if intentos >= 3:
            print("Tarjeta bloqueada")
            break
        else:
            print("Clave invalida")

    continuar = input("¿Desea realizar otra operación? (s/n): ")
    if continuar.lower() != 's':
        break
      