#Cajero Automático
usuario=int(input())
clave1=int(input())
monto=int(input())
if usuario==10334151:
    if clave1==1803:
        print("Monto a retirar")
        if monto>100000:
            print("monto no permitido")
        else:
            print("saldo cuenta=",100000-monto)
            print("saldo cajero=",1000000-monto)
    else:
        print("clave invalida")
        clave2=int(input())
        if clave2==1803:
            print("Monto a retirar")
            if monto>100000:
                print("monto no permitido")
            else:
                print("saldo cuenta",100000-monto)
                print("saldo cajero",1000000-monto)
        else:
             print("clave invalida")
             clave3=int(input())
             if clave3==1803:
                 print("Monto a retirar")
                 if monto>100000:
                     print("monto no permitido")
                 else:
                     print("saldo cuenta",100000-monto)
                     print("saldo cajero",1000000-monto)
             else:
                 print("tarjeta bloqueada")
                 sys.exit
else:
    sys.exit



    