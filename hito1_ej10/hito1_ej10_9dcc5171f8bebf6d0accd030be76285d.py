saldo_cuenta = 100000
saldo_cajero = 1000000
intentos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")
    
    if usuario == "10334151" and clave == "1803":
        break
    else:
        intentos += 1
        if intentos == 3:
            print("Tarjeta bloqueada")
            exit()
        else:
            print("Clave inválida. Intente nuevamente.")

while True:
    try:
        monto = float(input("Ingrese el monto a retirar: "))
        break
    except ValueError:
        print("Monto no válido. Intente nuevamente.")

if monto > saldo_cuenta:
    print("Monto no permitido. Saldo insuficiente.")
else:
    saldo_cuenta -= monto
    saldo_cajero -= monto
    print("saldo cuenta={}".format(saldo_cuenta))
    print("saldo cajero={}".format(saldo_cajero))
