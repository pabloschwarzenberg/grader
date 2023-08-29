saldo_cuenta = 100000
saldo_cajero = 1000000
intentos = 0

while intentos < 3:
    usuario = input("Ingrese el usuario: ")
    clave = input("Ingrese la clave: ")

    if usuario == "10334151" and clave == "1803":
        while True:
            monto_retiro = float(input("Ingrese el monto a retirar: "))

            if monto_retiro <= saldo_cuenta and monto_retiro <= saldo_cajero:
                saldo_cuenta -= monto_retiro
                saldo_cajero -= monto_retiro
                print("Retiro exitoso.")
                print("Saldo cuenta=", saldo_cuenta)
                print("Saldo cajero=", saldo_cajero)
            else:
                print("Monto no permitido.")
            
            continuar = input("¿Desea realizar otra transacción? (S/N): ")
            if continuar.upper() != "S":
                break
        break
    else:
        print("Clave inválida. Intente nuevamente.")
        intentos += 1

    if intentos == 3:
        print("Tarjeta bloqueada. Contacte al banco.")
        break

print("Gracias por utilizar nuestro cajero automático.")

      