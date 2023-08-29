saldo = 100000
caja = 1000000
b20 = 20
b10 = 40
b5 = 40

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
            if sa % 5000 != 0:
                print('Monto no valido solo se pueden retirar multiplos de 5000')
                exit(0)

            b20r = min(b20, sa // 20000)
            sa -= b20r*20000

            b10r = min(b10, sa // 10000)
            sa -= b10r*10000

            b5r = min(b5, sa // 5000)
            sa -= b5r*5000

            if sa > 0:
                print('No hay suficientes billetes para entregar')
                exit(0)

            saldo -= (b20r*20000 + b10r*10000 + b5r*5000)
            caja -= (b20r*20000 + b10r*10000+ b5r*5000)

            print('Saldo cuenta=' +str(saldo),' Saldo cajero='+str(caja))
            print('Billetes 20000 =', b20r)
            print('Billetes 10000 =', b10r)
            print('Billetes 5000 =', b5r)
            break
        else:
            count_error+= 1
            print('Error, intente de nuevo')

    if count_error == 3:
        print('Tarjeta bloqueada')
        exit(0)