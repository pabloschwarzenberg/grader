usuario = int(input("Ingrese usuario: "))
clave = int(input("Ingrese clave: "))
intentos = 1
saldo_cajero = 1000000
saldo_usuario = 100000
usuario = 10334151
contraseña = 1803
billetes_20 = 20000
billetes_10 = 10000
billetes_5 = 5000
def bills(d, x):
    billetes = d // x
    resto = d % x
    return billetes, resto
while clave != contraseña:
    intentos += 1
    if clave == contraseña:
        print("clave incorrecta")
        break
    if intentos > 3:
        break
    print("clave invalida")
    clave = int(input("Ingrese de nuevo su clave: "))
if intentos > 3:
    print("tarjeta bloqueada")
if usuario == usuario:
    if clave == contraseña:
        monto = int(input("¿Cuanto quiere retirar?: "))
        if monto > saldo_usuario and monto > saldo_cajero:
            print("monto no perimitido")
        else:
            saldo_usuario -= monto
            saldo_cajero -= monto
            c, r = bills(monto, billetes_20)
            e, r = bills(r, billetes_10)
            k, r = bills(r, billetes_5)
            print("saldo cuenta=" + str(saldo_usuario))
            print("saldo cajero=" + str(saldo_cajero))
            print("billetes20000=" + str(c))
            print("billetes10000=" + str(e))
            print("billetes5000=" + str(k))