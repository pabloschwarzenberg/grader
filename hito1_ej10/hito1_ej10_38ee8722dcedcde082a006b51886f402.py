#Cajero Automático
saldo_inicial_cuenta = 100000
saldo_inicial_cajero = 1000000
intentos_maximos = 3

usuario_valido = 10334151
clave_valida = 1803

saldo_cuenta = saldo_inicial_cuenta
saldo_cajero = saldo_inicial_cajero
intentos = 0

while intentos < intentos_maximos:
    usuario = int(input("Ingrese su usuario: "))
    clave = int(input("Ingrese su clave: "))

    if usuario == usuario_valido and clave == clave_valida:
        monto_retiro = float(input("Ingrese el monto a retirar: "))

        if monto_retiro > saldo_cuenta:
            print("Monto no permitido. El saldo de su cuenta es insuficiente.")
        elif monto_retiro > saldo_cajero:
            print("Monto no permitido. El cajero no dispone de suficiente dinero.")
        else:
            saldo_cuenta -= monto_retiro
            saldo_cajero -= monto_retiro
            print("Retiro exitoso.")
            print("Saldo cuenta:", saldo_cuenta)
            print("Saldo cajero:", saldo_cajero)
            break
    else:
        print("Clave inválida.")
        intentos += 1

if intentos == intentos_maximos:
    print("Tarjeta bloqueada.")
     