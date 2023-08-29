#Cajero Automático
usuario = int(input('Ingrese su N° de usuario: '))
MontoInicialUsuario = 100000
MontoInicialCajero = 1000000
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
        flag = False
        print('saldo cuenta=',saldoFinalUsuario)
        print('saldo cajero=',saldoFinalCajero)
      