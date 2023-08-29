#Cajero Automático
usuario = { 
    'usuario' : 10334151,
    'clave' : 1803,
    'saldo' : 100000
    
}

billetes = {
    '20mil' : [20,20],
    '10mil' : [40,40],
    '5mil' : [40,40]
}

cajero = 1000000
intento = 3



while intento > 0:
    if usuario['clave'] == int(input()):
        while True:
            monto = int(input())
            
            if usuario['saldo'] >= monto:
                usuario['saldo'] -= monto
                cajero -= monto
                break
        
            else:
                print('monto no permitido')
                
        break
    
    else:
        print('clave invalida')
        intento -= 1


        
    
if intento == 0:
    print('tarjeta bloqueada')
    
else:
    while monto > 0:
        if (monto//10000)%2 == 0 and (monto//10000) > 0 and billetes['20mil'][0] > 0:
            #print('2', monto//10000, (monto//10000)%2, monto)
            monto -= 20000
            billetes['20mil'][0] -= 1
            
        elif (monto//10000) > 0 and billetes['10mil'][0] > 0:
            #print('1', monto//10000, (monto//10000)%2, monto)
            monto -= 10000
            billetes['10mil'][0] -= 1
            
        elif (monto//1000)%5 == 0 and billetes['5mil'][0] > 0:
            #print('5', monto//10000, (monto//10000)%2, monto)
            monto -= 5000
            billetes['5mil'][0] -= 1
        
    print('saldo cuenta=' + str(usuario['saldo']))
    print('saldo cajero=' + str(cajero))
    print('billetes 20000=' + str(billetes['20mil'][1] - billetes['20mil'][0]))
    print('billetes 10000=' + str(billetes['10mil'][1] - billetes['10mil'][0]))
    print('billetes 5000=' + str(billetes['5mil'][1] - billetes['5mil'][0]))
    
    