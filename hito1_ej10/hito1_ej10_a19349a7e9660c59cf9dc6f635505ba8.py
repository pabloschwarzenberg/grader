#Cajero Automático
saldo_inicial = 1000000
saldo_cajero = 1000000

usuario_valido = 10334151
clave_valida = 1803

intentos = 0
usuario = int(input("Ingrese su usuario: "))
clave = int(input("Ingrese su clave: "))

if usuario == usuario_valido and clave == clave_valida:
    saldo_cuenta = 100000
    while intentos < 3:
        monto_retiro = int(input("Ingrese el monto a retirar: "))

        if monto_retiro > 0:
            if monto_retiro <= saldo_cuenta and monto_retiro <= saldo_cajero:
                saldo_cuenta -= monto_retiro
                saldo_cajero -= monto_retiro
                print("Retiro exitoso.")
                print("Saldo cuenta=", saldo_cuenta)
                print("Saldo cajero=", saldo_cajero)
                break
            elif monto_retiro > saldo_cuenta:
                print("Monto no permitido. Fondos insuficientes en la cuenta.")
            else:
                print("Monto no permitido. Fondos insuficientes en el cajero.")
        else:
            print("Monto no permitido. Ingrese un monto válido.")

        intentos += 1

    if intentos == 3:
        print("Tarjeta bloqueada.")
else:
    print("Clave inválida. Tarjeta bloqueada.")