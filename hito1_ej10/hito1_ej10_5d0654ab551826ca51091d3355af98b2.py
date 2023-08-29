#Cajero Automático
usuario=int(input())
x="N"
while x=="N":
    a=2
    clave=1803
    user=int(input())
    dv=1
    while clave!=user:
        if a>0:
            a-=1
            print("clave invalida")
            print("reingrese clave ")
            user=int(input())
        else:
            dv=0
            break
    if dv==0:
        print("tarjeta bloqueada")
    else:
        monto=int(input("ingrese monto "))
        if monto>100000:
            print("monto invalido")
        else:
            print("saldo cuenta=",100000-monto)
            print("saldo cajero=",1000000-monto)
        x=str(input())
            