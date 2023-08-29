#Cajero Automático
cont = 0
saldo_cajero = 1000000
saldo_cuenta = 100000
while cont < 3:
    print('-- Saldo cajero: '+str(saldo_cajero)+' --')
    usuario = int(input('Ingrese número de usuario: '))
    clave = int(input('Ingrese clave: '))

    if usuario == 10334151:
        if (clave != 1803):
            print('clave invalida')
            cont = cont + 1

        else:

            print('-- Saldo cuenta: '+str(saldo_cuenta)+' --')
            monto = int(input('-- Cuanto es el monto deseado a retirar: '))
            if (monto > saldo_cajero) or (monto > saldo_cuenta):
                print('monto no permitido')
            else:
                saldo_cajero = saldo_cajero - monto
                saldo_cuenta = saldo_cuenta - monto
                print('saldo cuenta='+str(saldo_cuenta))
                print('saldo cajero='+str(saldo_cajero))
                letra = input('Si ingresas la letra N sigues en el programa: ')
                if letra != 'N':
                    break
                      
    else:
        continue
        
            
if cont == 3:
    print('tarjeta bloqueada')