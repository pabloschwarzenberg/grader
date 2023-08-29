#Cajero Automático
cajero=1000000
usuario=10334151
clave=1803
dineroencuenta=100000
cont=1
while cont<=3:
    x=int(input("ingresa usuario:"))
    b=int(input("ingresa clave:"))
    if usuario==x and clave==b:
        monto=int(input("cuanto desea retirar:"))
        if monto>100000:
            print("monto no permitido")
        elif monto<=100000:
            dineroencuenta=dineroencuenta-monto
            cajero=cajero-monto
            print("saldo cuenta =",dineroencuenta)
            print("saldo cajero =",cajero)
            cont=4
            
    else:
        cont+=1
    if cont==4:
        print("tarjeta bloqueada")      