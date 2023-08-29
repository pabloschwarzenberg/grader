saldo_cajero = 1000000
saldo_cuenta = 100000
intentos = 0

while intentos < 3:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")
    if usuario == "10334151" and clave == "1803":
        print("Saldo actual:", saldo_cuenta)
        monto = int(input("Ingrese el monto a retirar: "))
        if monto > saldo_cuenta:
            print("Monto no permitido")
        else:
            saldo_cuenta -= monto
            saldo_cajero -= monto
            print("Saldo cuenta=", saldo_cuenta)
            print("Saldo cajero=", saldo_cajero)
        break
    else:
        print("Clave inválida")
        intentos += 1

if intentos == 3:
    print("Tarjeta bloqueada")


