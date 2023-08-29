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
    if clave==1803:
        print('clave validad')
        acceso(clave)
        
def acceso(clave):
    retiro = 0
    saldo=int(100000)
    cajero=int(1000000)
    while retiro<=saldo:
        retiro=int(input('monto a retirar: '))
        if retiro<=saldo:
            print('saldo cuenta=',saldo-retiro)
            print('saldo cajero=',cajero-retiro)
            salir=input('¿desea continuar? (S o N): ')
            if salir!='N':
                break
            saldo=saldo-retiro
            cajero=cajero-retiro
        else:
            print('monto no permitido')
            return acceso(clave)

            
 

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
