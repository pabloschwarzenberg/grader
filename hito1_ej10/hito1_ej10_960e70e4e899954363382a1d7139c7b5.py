def monto(monto,cajero=1000000,usuario=100000):
    if monto > cajero:
        return "Monto no permitido"
    else:
        usuario = usuario-monto
        cajero = cajero-monto
        print("saldo cuenta=",usuario)
        print("saldo cajero=",cajero)
        return[usuario,cajero]

c = 0 
b = 0
intentos = 0
while b == 0:
    if c == 0:
        print("Usuario")
        input()
        print("Clave")
        clave = input()
        if clave == "1803":
            c = 1
        elif intentos == 2:
            print("Tarjeta bloqueada")
            break
        else:
            intentos += 1
    elif c == 1:
        print("Ingrese monto a retirar")
        p = input()
        di = "qwertyuiopñlkjhgfdsazxcvbnm,.-{}+´¿QWERTYUIOPÑLKJHGFDSAZXCVBNM"
        if p in di:
            break
        elif p == "N":
            c = 1
        else:
            monto(float(p))