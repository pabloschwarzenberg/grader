def Monto(monto,Cajero=1000000,usuario=100000):
    if monto > Cajero:
        return "Monto no permitido"
    else:
        usuario = usuario-monto
        Cajero = Cajero-monto
        print("saldo cuenta=",usuario)
        print("saldo cajero=",Cajero)
        return [usuario,Cajero]

a = 0
b = 0
intentos = 0
while b == 0:
    if a == 0:
        print("Usuario")
        input()
        print("clave")
        clave = input()
        if clave == "1803":
            a = 1
        elif intentos == 2:
            print("Tarjeta bloqueada")
            break
        else:
            intentos += 1
    elif a == 1:
        print("Ingrese monto a retirar")
        p = input()
        di = "qwertyuiopñlkjhgfdsazxcvbm,.-{}+´¿QWERTYUIOPÑLKJHGFDSAZXCVBM"
        if p in di:
            break
        elif p == "N":
            c = 1
        else:
            Monto(float(p))
      