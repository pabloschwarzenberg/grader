#Cajero Automático
usuario = eval(input('ingrese su usuario: '))
clave = eval(input('ingrese su clave: '))

saldo = 100000
cajero = 1000000

if clave != 1803:
  print('clave invalida')
  clave = eval(input('ingrese su clave: '))
if clave != 1803:
  print('clave invalida')
  clave = eval(input('ingrese su clave: '))
if clave != 1803:
  print('tarjeta bloqueada')
else:
    if clave == 1803:
      monto = eval(input('monto a retirar: '))
      if monto > 100000:
        print('monto no permitido')

    print('saldo cuenta = ' ,saldo - monto)
    print('saldo cajero = ' ,cajero - monto)      