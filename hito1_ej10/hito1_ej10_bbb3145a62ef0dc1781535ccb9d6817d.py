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

q = 0
w = 0
intentos = 0
while w == 0:
    if q == 0:
        print("Usuario")
        input()
        print("clave")
        clave = input()
        if clave == "1803":
            q = 1
        elif intentos == 2:
            print("Tarjeta bloqueada")
            break
        else:
            intentos += 1
    elif q == 1:
        print("Ingrese monto a retirar")
        e = input()
        di = "qwertyuiopñlkjhgfdsazxcvbm,.-{}+´¿QWERTYUIOPÑLKJHGFDSAZXCVBM"
        if e in di:
            break
        elif e == "N":
            q = 1
        else:
            Monto(float(e))      