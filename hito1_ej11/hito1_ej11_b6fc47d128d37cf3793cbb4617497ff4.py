c=1000000
d=100000
g=20 #20.000
h=40 #10.000
i=40 #5.000
f=0
while f<3:
    a=int(input("ingrese usuario:"))
    b=int(input("ingrese clave:"))
    if a==10334151 and b==1803:
        e=int(input("ingrese monto a retirar:"))
        if e>=d or e<0:
               print("monto no permitido")
        elif e%5000!=0:
            print("monto no permitido")
        else:
               print("saldo cuenta=",d-e)
               print("saldo cajero=",c-e)
               j=e//10000
               k=(e//1000)%10
               l=k//5
               print("billetes 20000=0")
               print("billetes 10000=",j)
               print("billetes 5000=",l)
                    
                   
               break
    else:
            print("clave invalida")
            f=f+1
if f==3:
    print("tarjeta bloqueada")                
                     