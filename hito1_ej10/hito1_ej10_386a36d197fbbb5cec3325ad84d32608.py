#Cajero Automático
cont=1
totalc=1000000
persona=10334151
c=1803
saldo_cuenta=100000
opcion=0
while(cont!=3) and (opcion!="Y"):
    usuario=int(input("Ingrese ID: "))
    clave=int(input("Ingrese clave: "))
    if(usuario==persona and clave==c):
        monto_retiro=int(input("¿cuanto dinero va a retirar?: "))
        if(monto_retiro<=saldo_cuenta):
            totalc=totalc-monto_retiro
            saldo_cuenta=saldo_cuenta-monto_retiro
        else:
            print("monto no permitido")
    if(clave!=c):
        print("clave invalida")
        cont=cont+1
        
    print("desea hacer otra operacion o salir")
    print("N) otra operacion")
    print("Y) salir")
    opcion=input("Ingrese opcion: ")
    
print("saldo cuenta= ", saldo_cuenta)
print("saldo cajero= ",totalc)
if(cont==3):
    print("tarjeta bloqueada")      