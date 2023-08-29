#Cajero Automático
usuario = int(input('Ingrese su usuario: '))

while usuario != 10334151:
    usuario = input('Error, Ingrese su usuario: ')
clave = int(input('Ingrese su clave:'))

i = 0
saldoCajero = 1000000
bi20 = 20
bi10 = 40
bi5 = 40
retira20 = 0
retira10 = 0
retira5 = 0
while not clave == 1803:
    if i < 2:
        print('clave invalida')
        clave = int(input('Ingrese su clave: '))
        i = i + 1
        if i == 3:
            print('tarjeta bloqueada')
            break
saldo1803=100000
if i !=3:
    if clave == 1803:
        monto = int(input('Monto a retirar: '))
        if monto > saldo1803 and monto < 0:
            print('monto no permitido')
            monto = int(input('Error. Monto a retirar: '))
        else:
            saldo1803 = saldo1803 - monto
            nuevoSaldoCajero = saldoCajero - monto
            while monto > 0:
                if monto >= 20000 and bi20 > 0:
                    retira20 = retira20 + 1
                    bi20 = bi20 - 1
                    monto = monto - 20000
                if monto >= 10000 and bi10 > 0:
                    retira10 = retira10 + 1
                    bi10 = bi10 - 1
                    monto = monto - 10000
                if monto >= 5000 and bi5 > 0:
                    retira5 = retira5 + 1
                    bi5 = bi5 - 1
                    monto = monto - 5000
            print('saldo cuenta=', saldo1803)
            print('saldo cajero=', nuevoSaldoCajero)
            print("billetes 20000=",retira20)
            print("billetes 10000=",retira10)
            print("billetes 5000=",retira5)