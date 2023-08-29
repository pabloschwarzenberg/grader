#Cajero Automático
saldo_cajero = 1000000
usuario = "10334151"
clave ="1803"
saldo_usuario = 100000

while True:
    u = input("Ingrese su código de usuario:")
    if u!=usuario:
        continue
    elif u==usuario:
        c = input("Ingrese su clave:")
        for i in range(3):
             if c != clave:
                 print("clave invalida")
                 continue
             elif c == clave:
                 break
    if c != clave:
        print("tarjeta bloqueada")
        break
    elif c == clave:
        while True:
            monto = int(input("ingrese monto a retirar:"))
            if monto > saldo_usuario:
                print("monto no permitido")
                continue
            elif monto <= saldo_usuario:
                saldo_usuario = saldo_usuario-monto
                saldo_cajero = saldo_cajero-monto
                break
        print("saldo cuenta=",saldo_usuario)
        print("saldo cajero=",saldo_cajero)
        break
                