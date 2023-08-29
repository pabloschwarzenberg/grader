#Cajero Automático
cajero_automatico=1000000
usuario=[10334151,1803,100000]
s=int(input("Ingrese usuario:"))
b=int(input("Ingrese clave:"))
usua=[s,b]
cont=1
lista=[0,0]
while usua[1]!=usuario[1] and cont<3:
    print("Clave invalida")
    b=int(input("Ingrese clave:")) 
    cont=cont+1
    if cont==3 and b!=usuario[1]:
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
        cajero_automatico=cajero_automatico-int(c)
        t=str(usuario[2])
        u=str(cajero_automatico)
        lista[0]="saldo cuenta="+t
        lista[1]="saldo cajero="+u
        print(lista)

 

  
        
       

      