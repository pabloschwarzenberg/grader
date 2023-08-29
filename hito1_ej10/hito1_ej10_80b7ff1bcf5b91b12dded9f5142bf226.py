#Cajero Automático
import sys
usuario=int(input("ingrese usuario"))
clave=int(input("ingrese clave"))
i=0
saldo_cajero=1000000
saldo_usuario=100000


if usuario==10334151 and clave!=1803:
    print("clave invalida")
    i=i+1
    if i==3:
        print("tarjeta bloqueada")
        sys.exit()
elif usuario==10334151 and clave==1803:
    monto=int(input("ingrese monto a retirar"))
    if monto>saldo_cajero or monto>saldo_usuario:
        print("monto no permitido")
    elif monto<saldo_cajero and monto<=saldo_usuario:
        saldo_usuario=saldo_usuario-monto
        saldo_cajero=saldo_cajero-monto
        print("saldo cuenta= ", saldo_usuario)
        print("saldo cajero= ", saldo_cajero)
        
