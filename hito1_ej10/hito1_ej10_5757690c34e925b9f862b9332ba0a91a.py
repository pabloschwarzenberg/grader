saldo_inicial = 1000000
saldo_usuario = 100000
intentos_maximos = 3
usuario_valido = "10334151"
clave_valida = "1803"

saldo_cuenta = saldo_usuario
saldo_cajero = saldo_inicial

intentos = 0

while intentos < intentos_maximos:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == usuario_valido and clave == clave_valida:
        monto_retiro = float(input("Ingrese el monto a retirar: "))

        if monto_retiro <= saldo_cuenta and monto_retiro > 0:
            saldo_cuenta -= monto_retiro
            saldo_cajero -= monto_retiro

            print("Retiro exitoso.")
            print("Saldo cuenta=", saldo_cuenta)
            print("Saldo cajero=", saldo_cajero)

            break
        else:
            print("Monto no permitido.")
    else:
        print("Clave inválida.")
        intentos += 1

if intentos == intentos_maximos:
    print("Tarjeta bloqueada.")
