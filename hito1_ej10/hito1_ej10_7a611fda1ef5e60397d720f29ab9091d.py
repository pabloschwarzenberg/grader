#Cajero Automático
saldo_cuenta = 100000
saldo_cajero = 1000000
intentos_fallidos = 0

usuario_valido = 10334151
clave_valida = 1803

usuario = int(input("Ingrese su usuario: "))
clave = int(input("Ingrese su clave: "))

while usuario != usuario_valido or clave != clave_valida:
    intentos_fallidos += 1
    if intentos_fallidos == 3:
        print("Tarjeta bloqueada. Ha excedido el número máximo de intentos.")
        exit()
    print("Clave inválida. Por favor, ingrese nuevamente.")
    usuario = int(input("Ingrese su usuario: "))
    clave = int(input("Ingrese su clave: "))

monto_retiro = float(input("Ingrese el monto a retirar: "))

if monto_retiro <= 0 or monto_retiro > saldo_cuenta:
    print("Monto no permitido.")
else:
    saldo_cuenta -= monto_retiro
    saldo_cajero -= monto_retiro

    print("saldo cuenta=" + str(saldo_cuenta))
    print("saldo cajero=" + str(saldo_cajero))