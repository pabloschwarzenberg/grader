saldo_cajero = 1000000
saldo_cuenta = 100000
intentos_fallidos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")
    monto_retiro = 0
    
    if usuario == "10334151" and clave == "1803":
        while intentos_fallidos < 3:
            monto_retiro = int(input("Ingrese el monto que desea retirar: "))
            if monto_retiro % 10000 != 0 or monto_retiro <= 0:
                print("Monto no permitido")
            elif monto_retiro <= saldo_cuenta and monto_retiro <= saldo_cajero:
                saldo_cuenta -= monto_retiro
                saldo_cajero -= monto_retiro
                print("Retiro exitoso")
                print("Saldo cuenta: ", saldo_cuenta)
                print("Saldo cajero: ", saldo_cajero)
                break
            else:
                print("Saldo insuficiente en su cuenta o en el cajero")
            intentos_fallidos += 1
        else:
            print("Tarjeta bloqueada")
            break
    else:
        print("Clave invalida")
    
    opcion = input("¿Desea realizar otra operacion? (S/N): ")
    if opcion.upper() != "S":
        break