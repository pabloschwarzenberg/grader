#Cajero Automático
saldo_cuenta = 100000
saldo_cajero = 1000000
intentos = 0
usuario_valido = 10334151
clave_valida = 1803

while intentos < 3:
    usuario = input("Ingrese su número de usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == str(usuario_valido) and clave == str(clave_valida):
        while True:
            try:
                monto_retiro = float(input("Ingrese el monto a retirar: "))

                if monto_retiro <= saldo_cuenta and monto_retiro <= saldo_cajero:
                    saldo_cuenta -= monto_retiro
                    saldo_cajero -= monto_retiro
                    print("Retiro exitoso.")
                    print("Saldo cuenta=" + str(saldo_cuenta))
                    print("Saldo cajero=" + str(saldo_cajero))
                    break
                elif monto_retiro > saldo_cuenta:
                    print("Monto no permitido. Saldo insuficiente en la cuenta.")
                elif monto_retiro > saldo_cajero:
                    print("Monto no permitido. Saldo insuficiente en el cajero.")
            except ValueError:
                print("Error: Ingrese un monto válido.")
        break
    else:
        intentos += 1
        print("Clave inválida.")

    if intentos == 3:
        print("Tarjeta bloqueada.")