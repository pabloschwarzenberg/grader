#Hito 1 Cajero
saldocajero=1000000
saldousuario=100000
intentosFallidos=0
x=0
a=0
g=input()
while a!='N':
   
    a=(input())
    b=1
    if a!='N':
        if int(a)!=1803:
            intentosFallidos=1
        while intentosFallidos<3 and b==1:
            if int(a)!=1803:
                print("clave invalida")
                a=int(input())
                intentosFallidos=intentosFallidos+1
            else:
                print("monto a retirar")
                monto=int(input())
                if monto<=saldousuario:
                    print("saldo cuenta=",saldousuario-monto)
                    print("saldo cajero=",saldocajero-monto)
                    saldousuario=saldousuario-monto
                    saldocajero=saldocajero-monto
                    b=0
                else:
                    while monto>saldousuario:
                            print("monto no permitido")
                            monto=int(input())
                    print("saldo cuenta=",saldousuario-monto)
                    print("saldo cajero=",saldocajero-monto)
                    saldousuario=saldousuario-monto
                    saldocajero=saldocajero-monto
        if intentosFallidos==3:
            print("tarjeta bloqueada")
            intentosFallidos=0
            

            