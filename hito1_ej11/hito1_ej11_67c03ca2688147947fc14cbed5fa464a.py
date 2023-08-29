usuario = 10334151
clave = 1803
saldo = 1000000

saldo_usuario = 100000

u = int(input("Usuario: "))

intentos = 3
entrar = False
while not entrar:
    c = int(input("Contraseña: "))

    if c != clave:
        intentos -= 1
        if intentos == 0:
            print("tarjeta bloqueada")
            break
        else:
            print("clave invalida")
    else:
        entrar = True

while entrar:
    monto_retirar = int(input("Monto a retirar: "))
    if monto_retirar > saldo_usuario or monto_retirar > saldo:
        print("monto no permitido")
    else:
        saldo_usuario -= monto_retirar
        saldo -= monto_retirar

        print("saldo cuenta=" + str(saldo_usuario))
        print("saldo cajero=" + str(saldo))

        b20 = monto_retirar // 20000
        monto_retirar %= 20000
        b10 = monto_retirar // 10000
        monto_retirar %= 10000
        b5 = monto_retirar // 5000
        print("billetes 20000=" + str(b20))
        print("billetes 10000=" + str(b10))
        print("billetes 5000=" + str(b5))

    if input("Salir? (Y/N): ") != 'N':
        break