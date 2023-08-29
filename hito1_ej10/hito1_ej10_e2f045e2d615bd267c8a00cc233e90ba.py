#Cajero Automático

saldo = 100000
caja = 1000000
u = input('Ingrese el usuario:')

if u == '10334151':
    count_error = 0
    while count_error < 3:
        c = input('Ingrese su clave:')

        if c == '1803':
            sa = int(input('Ingrese monto a retirar:'))
            if sa > saldo:
                print('Saldo insuficiente')
                exit(0)
            saldo -= sa
            caja -= sa
            print('saldo cuenta=' + str(saldo), ' saldo cajero=' + str(caja))
            break
        else:
            count_error += 1
            print('Error, intente de nuevo')

    if count_error == 3:
        print('Tarjeta bloqueada')
        exit(0)
