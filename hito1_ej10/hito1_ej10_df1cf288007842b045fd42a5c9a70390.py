#Cajero Automático
usuario = { 
    'usuario' : 10334151,
    'clave' : 1803,
    'saldo' : 100000
    
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
    print('saldo cuenta=' + str(usuario['saldo']))
    print('saldo cajero=' + str(cajero))
    