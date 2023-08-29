#Cajero Automático
contador=0
a=0
S='N'
while S=='N':
    if S!='N':
        break
    if S=='N':
        Usuario =int(input('Usuario: '))
        if Usuario == 10334151:
            Clave=int(input('clave: '))
            while Clave!=1803:
                contador=contador+1
                if contador==3:
                    print('tarjeta bloqueada')
                    a=1
                    S="n"
                    break
                if contador<3:
                    print('Clave invalida')
                    Clave=int(input('clave: '))
            if Clave==1803:
                Money=int(input('¿Cuánto dinero desea retirar?: '))
                if Money>100000 or Money<0:
                    print('monto no permitido')
                else:
                    S="n"
                    print('saldo cuenta=',100000-Money,',saldo cajero=',1000000-Money)
                    a=1
                    break
        elif Usuario!= 10334151:
            print('Usuario incorrecto')
        if a==1:
            break