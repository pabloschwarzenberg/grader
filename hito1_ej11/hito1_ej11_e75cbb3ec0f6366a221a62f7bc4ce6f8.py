#Cajero Automático
usuario = int(input('Ingrese su N° de usuario: '))
MontoInicialUsuario = 100000
MontoInicialCajero = 1000000
BilletesDe20 = 20
BilletesDe10 = 40
BilletesDe5 = 40
errores = 0
while errores < 3:
    clave = int(input('Ingrese su clave: '))
    if usuario != 10334151 and clave != 1803:
        print('clave invalida')
        errores += 1
    else:
        break

if errores == 3:
    print('tarjeta bloqueada')
    exit()

flag = True
while flag:
    retiro = int(input('Ingrese un monto: '))
    saldoFinalUsuario = MontoInicialUsuario - retiro
    saldoFinalCajero = MontoInicialCajero - retiro
    if saldoFinalUsuario < 0 or saldoFinalCajero < 0:
        print('monto no permitido')
    else:
        print('saldo cuenta=',saldoFinalUsuario)
        print('saldo cajero=',saldoFinalCajero)
        flag = False
        count20 = 0
        count10 = 0
        count5 = 0
        while retiro >= 20000 and BilletesDe20 != 0:
            retiro -= 20000
            count20 += 1

        while retiro >= 10000 and BilletesDe10 != 0:
            retiro -= 10000
            count10 += 1

        while retiro >= 5000 and BilletesDe5 != 0:
            retiro -= 5000
            count5 += 1


        print('billetes 20000=',count20)
        print('billetes 10000=', count10)
        print('billetes 5000=', count5)

