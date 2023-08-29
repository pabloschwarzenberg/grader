#Cajero Automático
saldo_cajero = 1000000

usuario_rut = '10334151'
usuario_clave = '1803'
usuario_saldo = 100000

while True:
    intentos = 0
    rut = input()

    if rut != 'N':
        break

    if rut == usuario_rut:
        for i in range(3):
            clave = input()
            if clave == usuario_clave:
                break

            else:
                print('clave invalida')
                intentos += 1

        if intentos == 3:
            print('tarjeta bloqueada')
            break
        
        while True:
            algo = input()
            if algo != 'N':
                break
            monto = int(input())
            if monto < 5000 or monto > saldo_cajero or monto > usuario_saldo:
                print('monto no permitido')
                continue
            
            usuario_saldo -= monto
            print(['saldo cuenta=' + str(usuario_saldo), 'saldo cajero=' + str(saldo_cajero)])


      