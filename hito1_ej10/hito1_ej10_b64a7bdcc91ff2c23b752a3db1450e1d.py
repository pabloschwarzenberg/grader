#Cajero Automático
def saldo(monto,Cajero=1000000,usuario=100000):
    if monto > Cajero:
        return "Monto no permitido"
    else:
        usuario = usuario-monto
        Cajero = Cajero-monto
        print("saldo cuenta=",usuario)
        print("saldo cajero=",Cajero)
        return [usuario,Cajero]

cont = 0
cont1 = 0
intentos = 0
while cont1 == 0:
    if cont == 0:
        print("Usuario")
        input()
        print("clave")
        clave = input()
        if clave == "1803":
            cont = 1
        elif intentos == 2:
            print("Tarjeta bloqueada")
            break
        else:
            intentos += 1
    elif cont == 1:
        print("Ingrese monto a retirar")
        p = input()
        di = "qwertyuiopñlkjhgfdsazxcvbm,.-{}+´¿QWERTYUIOPÑLKJHGFDSAZXCVBM"
        if p in di:
            break
        elif p == "N":
            cont = 1
        else:
            saldo(float(p))