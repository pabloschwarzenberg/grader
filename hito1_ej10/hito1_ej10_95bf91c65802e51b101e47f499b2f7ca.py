monto=1000000
usr=100000
intentos=3
while intentos!=0: 
    usuario=input()
    clave=int(input())
    if usuario=="10334151" and clave==1803:   
        dinero=int(input())
        if dinero>usr or dinero>monto:
            print("monto no permitido")

        elif dinero<=usr:
            usr=usr-dinero
            monto=monto-dinero
            print("saldo cuenta=",usr)
            print("saldo cajero=",monto)
            
    elif clave!= 1803 and usuario=="10334151":
        intentos= intentos-1
        print("clave invalida")
    else:
        break

if intentos == 0:
        print("tarjeta bloqueada")