#Cajero Automático
def verificacion(clave):
    i=1
    while i<3 and clave!=1803:
        clave=int(input('ingrese clave: '))
        if i==1 and clave!=1803:
            print('clave invalidad')
        elif i==2 and clave!=1803:
            print('tarjeta bloqueada')
        i=i+1
    if clave!=1803:
        print('clave validad')
        acceso(clave)
        
def acceso(clave):
    retiro = 0
    saldo=int(100000)
    cajero=int(1000000)
    nb20000 = 0
    nb10000 = 0
    nb5000 = 0
    nbT20000 = 20
    nbT10000 = 40
    nbT5000 = 40
    while retiro<=saldo:
        retiro = int(input('monto a retirar: '))
        if retiro<=saldo:
            print('saldo cuenta=',saldo-retiro)
            print('saldo cajero=',cajero-retiro)
            while retiro>0:
                if retiro>=20000:
                    nb20000 = nb20000 + 1
                    retiro = retiro - 20000
                elif retiro>=10000:
                    nb10000 = nb10000 + 1
                    retiro = retiro - 20000
                elif retiro==5000:
                    nb5000 = nb5000 + 1
                    retiro = retiro - 20000
        else:
            print('monto no permitido')
            return acceso(clave)
        print('billetes 20000=',nb20000)
        print('billetes 10000=',nb10000)
        print('billetes 5000=',nb5000)

        
        salir=input('¿desea salir? (S o N): ')
        if salir!='N':
            break
        saldo=saldo-retiro
        cajero=cajero-retiro
        nbT20000 = nbT20000 - nb20000
        nbT10000 = nbT10000 - nb20000
        nbT5000 = nbT5000 - nb5000
        
usuario=int(input('ingrese usuario: '))
if usuario==10334151:
    i=1
    clave=int(input('ingrese clave: '))
    if clave == 1803:
        print('clave valida')
        acceso(clave)
    else:
        print('clave invalida')
        verificacion(clave)
