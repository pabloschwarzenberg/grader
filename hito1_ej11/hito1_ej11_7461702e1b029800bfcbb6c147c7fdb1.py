#Cajero Automático
def distribuye_billetes(monto):

    cont20000 = 0
    cont10000 = 0
    cont5000 = 0
    suma=0
    while monto > 0:
        if monto >= 20000:
            cont20000 = cont20000 + 1
            monto = monto - 20000
        elif monto >= 10000:
            cont10000 = cont10000 + 1
            monto = monto - 10000
        elif monto >= 5000:
            cont5000 = cont5000 + 1
            monto = monto - 5000
    suma1=cont20000*20000
    suma2=cont10000*10000
    suma3=cont5000*5000
    suma=suma1+suma2+suma3
    return [cont20000, cont10000, cont5000,suma]   

def retirar_dinero():
    saldo_cajero=1000000
    saldo_usuario=100000
    retiro=int(input('ingrese la cantidad de dinero a retirar'))
    while retiro>saldo_cajero or retiro>saldo_usuario:
        print('monto no permitido')
        retiro=int(input('ingrese la cantidad de dinero a retirar'))
    if retiro<=saldo_cajero and retiro<=saldo_usuario:
        saldo_cajero=saldo_cajero-retiro
        saldo_usuario=saldo_usuario-retiro
        x='saldo cuenta=' + str(saldo_usuario)
        y='saldo cajero=' + str(saldo_cajero)
        listaBilletes = distribuye_billetes(retiro)
        p1='billetes 20000=' + str(listaBilletes[0])
        p2='billetes 10000=' + str(listaBilletes[1])
        p3='billetes 5000=' + str(listaBilletes[2])
        p4='suma de billetes es=' + str(listaBilletes[3])
        return (x,y,p1,p2,p3)


def ingresar_usuario():
    usuario=0
    c=0
    while usuario!=10334151:
        usuario=int(input('ingrese su usuario de 8 digitos'))
        if usuario==10334151:
            usuario=10334151
            break
    clave=0
    while clave!=1803:
        clave=int(input('ingrese clave del cajero'))
        c=c+1
        if clave!=1803:
            print('clave invalida')
        if c==3:
            print('tarjeta bloqueada')
            break
    if clave==1803:
        retirar=retirar_dinero()
        i=0
        while i<len(retirar):
            print(retirar[i])
            i=i+1

ingresar_usuario()    