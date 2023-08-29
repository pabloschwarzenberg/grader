#Cajero Automático
import sys
saldo=1000000
montocajero=100000
cont=1
continuar = 1
while continuar==1:
    
    usuario=int(input("ingrese usuario"))

    clave=int(input("ingrese clave"))
    if usuario==10334151:
    
        while clave!=1803:
            print("clave invalida")
            cont=cont+1
            clave=input("ingrese clave")
            if cont==3:
                sys.exit(1)
            
    monto=int(input("ingrese monto a retirar"))
    while monto>1000000:
        print("monto no permitido")
        monto=input("ingrese otro monto")
    
    montofinal=1000000-monto
    montocajero=montocajero-monto
    print("saldo cuenta=",montocajero)
    print("saldo cajero=",montofinal)


    continuar =input("desea continuar 1=s 0=n")
 

 



