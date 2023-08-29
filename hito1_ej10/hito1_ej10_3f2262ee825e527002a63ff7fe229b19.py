def monto(monto, cajero = 1000000,usuario = 100000):
    if monto > cajero:
        return"monto no permitido"
    else:
        usuario = usuario-monto
        cajero = cajero-monto
        print("saldo cuenta =", usuario)
        print("saldo cajero =", cajero)
        return[usuario,cajero]

c = 0
b = 0
intentos = 0

while b == 0:
    if c == 0:
        print("usuario")
        input()
        print("clave")
        clave = input()
        if clave == "1803":
            c = 1
        elif intentos == 2:
            print("tarjeta bloqueada")
            break
        else:
            intentos = intentos + 1

    elif c == 1:
        print("ingrese monto a retirar")
        p = input()
        di = "qwertyuiopñlkjhgfdsazxcvbnm,.-{}+'¿QWERTYUIOPÑLKJHGFDSAZXCVBNM"
        if p in di:
            break
        elif p == 0:
            c=1

        else:
            monto(float(p))