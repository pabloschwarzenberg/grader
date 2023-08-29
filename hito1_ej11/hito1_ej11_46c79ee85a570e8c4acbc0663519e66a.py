#Cajero Automático
user=  int(input('Usuario: '))
clave= int(input('Clave: '))

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


cuenta= 100000
cajero= 1000000
i=3

while i!= 0:
    if user== 10334151 and clave== 1803:
        reva_clave= int(input('Revalidar clave: '))
        if reva_clave== 1803:
            monto= input('Monto a retirar: ')
            if monto== 'N':
                break
            monto= int(monto)
            
            if monto> 100000:
                print('Monto no permitido')
            elif monto < 100000:
                L = nbEntregados(monto)
                cuenta= cuenta- monto
                cajero= cajero- monto
                print('saldo cuenta=' + str(cuenta))
                print('saldo cajero=' + str(cajero))
                print("billetes 20000=" + str(L[0]))
                print("billetes 10000=" + str(L[1]))
                print("billetes 5000=" + str(L[2]))
                
        if reva_clave!= 1803:
            print('clave invalida')
            i= i- 1
if i== 0:
    print('tarjeta bloqueada')

