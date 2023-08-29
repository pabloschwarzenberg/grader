#Cajero Automático
cajero=1000000
usuario=[10334151,1803,100000]
a=int(input("Ingresar usuario:"))
b=int(input("Ingresar clave:"))
usua=[a,b]
count=1
lista=[0,0]
bill_20=20
bill_10=40
bill_5=40
while usua[1]!=usuario[1] and count<3:
    print("Clave invalida")
    b=int(input("Ingresar clave:")) 
    count=count+1
    if count==3 and b!=usuario[1]:
        print("Tarjeta bloqueada")
        break
while usua[1]==usuario[1]and usuario[2]>0:
    c=(input("ingresar monto a retirar:"))
    if c=="Y":
        break
    if int(c)>usuario[2]:
        print("monto no permitido")
    if int(c)<=int(c):
        s=usuario[2]-int(c)
        usuario[2]=s
        cajero=cajero-int(c)
        t=str(usuario[2])
        u=str(cajero)
        lista[0]="saldo cuenta="+t
        lista[1]="saldo cajero="+u
        print(lista)
        