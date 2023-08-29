#Cajero Automático
usuario = str(input("Ingrese su usuario: "))
contrasena = str(input("Ingrese su contraseña: "))
intentos = 3
saldo_cajero = 1000000
saldo_cuenta = 100000
while intentos != 0:
    if contrasena != "1803":
        intentos -= 1
        contrasena = str(input("Clave inválida, quedan", intentos, "intentos: "))
    else:
        monto = int(input("Ingrese su monto a retirar: "))
        if monto < saldo_cuenta:
            saldo_cuenta = saldo_cuenta - monto
            saldo_cajero = saldo_cajero - monto
            print("Saldo cuenta=", saldo_cuenta)
            print("Saldo cajero=", saldo_cajero)
            break
        else:
            print("Monto inválido")
if intentos == 0:
    print("Tarjeta bloqueada")
