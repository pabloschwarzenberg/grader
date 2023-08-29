#Cajero Automático
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
        return (x,y)
        

def ingresar_usuario():
    usuario=0
    c=0
    lista=[]
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
        print(retirar)

ingresar_usuario()