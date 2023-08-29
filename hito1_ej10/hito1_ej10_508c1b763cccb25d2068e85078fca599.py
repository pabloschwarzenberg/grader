def Monto(monto, Cajero=1000000, usuario=100000):
    if monto > Cajero:
        return "Monto no permitido"
    else:
        usuario = usuario-monto
        Cajero = Cajero-monto
        print("Saldo cuenta= ", usuario)
        print("Saldo cajero= ", Cajero)
        return[usuario, Cajero]


b = 0
c = 0
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
        print("Ingrese monto para retirar: ")
        p = input()
        di = "qqwertyuiopñlkjhgfdsazxcvbnm,.{}+'¿QWERTYUIOPÑLKJHGFDSAZXCVBNM"
        if p in di:
            break
        elif p == "N":
            c = 1
        else:
            Monto(float(p))
