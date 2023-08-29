c=True
saldo=1000000
saldou=100000
contador=0
if c:
    a=int(input('usuario: '))
    b=int(input('clave: '))
    if a==10334151 and b==1803:
        d=int(input('monto: '))
        if d>100000 or d<0:
            print('monto no permitido')
        else:
            print('saldo cuenta=',saldou-d)
            print('saldo cajero=',saldo-d)
            e=d//20000
            f=d%20000
            if f>10000:
                g=f//10000
                h=f%10000
                i=h//5000
            else:
                g=0
                i=f//5000
            print('billetes 20000=',e)
            print('billetes 10000=',g)
            print('billetes 5000=',i)
    elif a==10334151 and not b==1803:
        print('clave invalida')
        contador=contador+1
        if contador==3:
            print('tarjeta bloqueada')
            c=False
    elif a!='N' or b!='N':
        c=False
