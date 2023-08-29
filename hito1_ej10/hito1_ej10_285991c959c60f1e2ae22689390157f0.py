#Cajero Automático
U=int(input("ingrese numero de usuario:"))
C=int(input("ingrese clave:"))
n=0

if(C!=1803)and (n<2):
    c=int(input("Clave invalida, ingrese denuevo:"))
    n=n+1
    if (n==2):
        print("tarjeta bloqueada")
        
if(C==1803):
    m=int(input("ingrese monto a retirar:"))
    if (0<=m<=100000):
        M=(100000-m)
        cajero=(1000000-m)
        print("saldo cuenta="+str(M))    
        print("saldo cajero="+str(cajero))   
    else:
        print("monto no permitido")

     