#Cajero Automático
cuenta=100000
cajero = 1000000
usuario = int(input("usuario="))
i=1
entro=False
#if(usuario==10334151):
while i <= 3:
    clave = int(input("clave="))
    if(usuario==10334151 and clave==1803):
        entro=True
        monto = int(input("monto a retirar="))
        if(monto > cuenta and monto <= 0 and monto > cajero):
            print("monto no permitido")
        else:
            cuenta=cuenta - monto
            cajero=cajero - monto
            print("saldo cuenta=" + str(cuenta))
            print("saldo cajero=" + str(cajero))
        break
    else:
        print("clave invalida")

    i = i + 1
if(entro==False):
    print("tarjeta bloqueada")     