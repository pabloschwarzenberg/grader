#Cajero Automático
b20000=20
b10000=40
b5000=40
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
            saldo=monto
            q20=int(monto/20000)
            saldo=saldo-20000*q20
            q10=int(saldo/10000)
            saldo=saldo-10000*q10
            q5=int(saldo/5000)
            
            cuenta=cuenta - monto
            cajero=cajero - monto
            print("saldo cuenta=" + str(cuenta))
            print("saldo cajero=" + str(cajero))
            if(q20 > 0):
                b20000=b20000-q20
                print("billetes 20000="+ str(q20))
            if(q10 > 0):
                b10000=b10000-q10
                print("billetes 10000="+ str(q10))
            if(q5 > 0):
                b5000=b5000-q5
                print("billetes 5000="+ str(q5))
                
        break
    else:
        print("clave invalida")

    i = i + 1
if(entro==False):
    print("tarjeta bloqueada")    