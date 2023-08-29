#Cajero Automático
u=input()
c=input()
scu=100000
sca=1000000
while (c==1803) and (u== 10334151):
    m=input()
    if (scu>=m):
        scu= (100000-m)
        sca= (1000000-m)
        print("saldo cuenta =",scu)
        print("saldo cajero =",sca)
    elif (scu<m):
        print("monto no permitido")
    scu=scu-m
    sca=sca-m
if (c!=1803) and (u==10334151):
    print("clave invalida")
elif (c!=1803):
    print("clave invalida")
elif (c!=1803):
    print("tarjeta bloqueada")
if (c!=1803) and (u==10334151):
    print("clave invalida")
elif (c!=1803):
    print("clave invalida")
elif (c==1803):
    while (c==1803) and (u== 10334151):
                m=input()
                if (scu>=m):
                    scu= (100000-m)
                    sca= (1000000-m)
                    print("saldo cuenta =",scu)
                    print("saldo cajero =",sca)
                if (scu<m):
                    print("monto no permitido")
                scu=scu-m
                sca=sca-m
if (c!=1803) and (u==10334151):
    print("clave invalida")
elif (c==1803):
    while (c==1803) and (u== 10334151):
        m=input("que monto desea retirar:")
        if (scu>=m):
            scu= (100000-m)
            sca= (1000000-m)
            print("saldo cuenta =",scu)
            print("saldo cajero =",sca)
        if (scu<m):
            print("monto no permitido")
            scu=scu-m
            sca=sca-m        