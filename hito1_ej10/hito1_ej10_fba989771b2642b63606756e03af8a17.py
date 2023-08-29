#Cajero Automático
def Monto(monto,Cajero=1000000,usuario=100000):
    if monto > Cajero:
        return "Monto no permitido"
    else:
        usuario = usuario-monto
        Cajero = Cajero-monto
        print("saldo cuenta=",usuario)
        print("saldo cajero=",Cajero)
        return [usuario,Cajero]

m = 0
a = 0
intentos = 0
while a == 0:
    if m == 0:
        print("Usuario")
        input()
        print("clave")
        clave = input()
        if clave == "1803":
            m = 1
        elif intentos == 2:
            print("Tarjeta bloqueada")
            break
        else:
            intentos += 1
    elif m == 1:
        print("Ingrese monto a retirar")
        t = input()
        di = "qwertyuiopñlkjhgfdsazxcvbm,.-{}+´¿QWERTYUIOPÑLKJHGFDSAZXCVBM"
        if t in di:
            break
        elif t == "N":
            m = 1
        else:
            Monto(float(t))