#Cajero Automático
usuario = int(input('ingresa número de usuario: '))
Saldo_Inicial = int(1000000)

def nbEntregados(monto):
    nb20000 = 0
    nb10000 = 0
    nb5000 = 0    
    while monto>0:
        if monto >= 20000:
            nb20000 = nb20000 + 1
            monto = monto - 20000
        elif monto >= 10000:
            nb10000 = nb10000 + 1
            monto = monto - 10000
        elif monto >= 5000:
            nb5000 = nb5000 + 1
            monto = monto - 5000
    return [nb20000, nb10000, nb5000]

nbT20000 = 20 
nbT10000 = 40 
nbT5000 = 40 



opcion = "N"

if usuario == 10334151:
    monto = int(100000)
    i = 1
    clave = int(input('ingresa número de Clave: '))
    if clave != 1803:
        while i < 3 and clave != 1803:
            if i < 3:
                print('clave invalida')
                clave = int(input('ingresa número de clave: '))
                i = i + 1
            if i == 3:
                print('tarjeta bloqueada')
                break

    while opcion == 'N':
        sacaDinero = int(input('monto a retirar: '))
        while sacaDinero > monto:
            print('monto no permitido')
            sacaDinero = int(input('cuanto deseas retirar: '))
            
        L = nbEntregados(sacaDinero)
        monto = monto - sacaDinero
        Saldo_Inicial = Saldo_Inicial - sacaDinero

        nbT20000 = 20 - L[0] 
        nbT10000 = 40 - L[1] 
        nbT5000 = 40 - L[2] 
    
        print('saldo cuenta=', monto)
        print('saldo cajero=', Saldo_Inicial)
        print("billetes 20000=" + str(L[0]))
        print("billetes 10000=" + str(L[1]))
        print("billetes 5000=" + str(L[2]))
        
        opcion = input('¿deseas seguir retirando dinero?: ')