saldo_cajero = 1000000
saldo_usuario = 100000
x = 'Y'
intentos = 0

# Valores de ejemplo para probar el funcionamiento del código
usuario = "10334151"
clave = "1803"
monto = 50000

while x != 'N':
    if intentos >= 3:
        print("Tarjeta bloqueada")
        break

    if usuario == 'N':
        x = 'N'
    elif usuario == '10334151':
        if clave == 'N':
            x = 'N'
        elif clave == '1803':
            if monto == 'N':
                x = 'N'
            else:
                monto = int(monto)
                if monto > saldo_usuario or monto > saldo_cajero:
                    print("Monto no permitido")
                else:
                    saldo_cajero -= monto
                    saldo_usuario -= monto
                    print("Saldo cuenta =", saldo_usuario)
                    print("Saldo cajero =", saldo_cajero)
        else:
            print("Clave inválida")
            intentos += 1
    else:
        print("Usuario inválido")
        intentos += 1
