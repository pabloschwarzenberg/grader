#Cajero Automático
import sys
usuario=int(input("Usuario: "))
if usuario!=10334151:
    sys.exit("usuario invlaido")
clave=int(input("clave: "))
if clave==1803:
    monto=int(input("monto a retirar:"))
    if monto>100000:
        sys.exit("monto no permitido")
    else:
        print("saldo cuenta =",100000-monto)
        print("saldo cajero =",1000000-monto)
else:
    print("clave invalida")
    clave2=int(input("clave: "))
    if clave2==1803:
        monto=int(input("monto a retirar:"))
        if monto>100000:
            sys.exit("monto no permitido")
        else:
            print("saldo cuenta =",100000-monto)
            print("saldo cajero =",1000000-monto)
    else:
        print("clave invalida")
        clave3=int(input("clave: "))
        if clave3==1803:
            monto=int(input("monto a retirar:"))
            if monto>100000:
                sys.exit("monto no permitido")
            else:
                print("saldo cuenta =",100000-monto)
                print("saldo cajero =",1000000-monto)
        else:
            sys.exit("tarjeta bloqueada")