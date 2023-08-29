#Cajero Automático
cajero=1000000
usuario=[10334151,1803,100000]
a=int(input("Ingrese usuario:"))
b=int(input("Ingrese clave:"))
usua=[a,b]
count=1
lista=[0,0]
bill_20=20
bill_10=40
bill_5=40
while usua[1]!=usuario[1] and count<3:
    print("Clave invalida")
    b=int(input("Ingrese clave:")) 
    count=count+1
    if count==3 and b!=usuario[1]:
        print("Tarjeta bloqueada")
        break
while usua[1]==usuario[1]and usuario[2]>0:
    c=(input("ingrese monto a retirar:"))
    if c=="Y":
        break
    if int(c)>usuario[2]:
        print("monto no permitido")
    if int(c)<=int(c):
        m=usuario[2]-int(c)
        usuario[2]=m
        cajero=cajero-int(c)
        t=str(usuario[2])
        u=str(cajero)
        lista[0]="saldo cuenta="+t
        lista[1]="saldo cajero="+u
        print(lista)
        b_20=(int(c)//20000)
        b_10=(int(c)-(b_20*20000))//10000
        b_5=((int(c)-(b_20*20000))%10000)//5000
        bill_20=bill_20-b_20
        bill_10=bill_10-b_10
        bill_5=bill_5-b_5
        print("billetes 20000=",b_20)
        print("billetes 10000=",b_10)
        print("billetes 5000=",b_5)        