c=1000000
d=100000
f=0
while f<3:
    a=int(input("ingrese usuario:"))
    b=int(input("ingrese clave:"))
    if a==10334151 and b==1803:
        e=int(input("ingrese monto a retirar:"))
        if e>=d or e<0:
               print("monto no permitido")
        else:
               print("saldo cuenta=",d-e)
               print("saldo cajero=",c-e)
               break
    else:
            print("clave invalida")
            f=f+1
if f==3:
    print("tarjeta bloqueada")                
               