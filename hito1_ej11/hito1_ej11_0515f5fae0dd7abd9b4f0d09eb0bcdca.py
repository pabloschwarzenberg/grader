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

billetes=[20000,10000,5000]
cantidad=[20,40,40]

if monto == 5000:
  print('billetes 20000 = 0')
  print('billetes 10000 = 0')
  print('billetes 5000 = 1')
elif monto == 10000:
  print('billetes 20000 = 0')
  print('billetes 10000 = 1')
  print('billetes 5000 = 0')
elif monto == 15000:
  print('billetes 20000 = 0')
  print('billetes 10000 = 1')
  print('billetes 5000 = 1')
elif monto == 20000:
  print('billetes 20000 = 1')
  print('billetes 10000 = 0')
  print('billetes 5000 = 0')
elif monto == 25000:
  print('billetes 20000 = 1')
  print('billetes 10000 = 0')
  print('billetes 5000 = 1')
elif monto == 30000:
  print('billetes 20000 = 1')
  print('billetes 10000 = 1')
  print('billetes 5000 = 0')
elif monto == 35000:
  print('billetes 20000 = 1')
  print('billetes 10000 = 1')
  print('billetes 5000 = 1')
elif monto == 40000:
  print('billetes 20000 = 2')
  print('billetes 10000 = 0')
  print('billetes 5000 = 0')
elif monto == 45000:
  print('billetes 20000 = 2')
  print('billetes 10000 = 0')
  print('billetes 5000 = 1')
elif monto == 50000:
  print('billetes 20000 = 2')
  print('billetes 10000 = 1')
  print('billetes 5000 = 0')
elif monto == 55000:
  print('billetes 20000 = 2')
  print('billetes 10000 = 1')
  print('billetes 5000 = 1')
elif monto == 60000:
  print('billetes 20000 = 3')
  print('billetes 10000 = 0')
  print('billetes 5000 = 0')
elif monto == 65000:
  print('billetes 20000 = 3')
  print('billetes 10000 = 0')
  print('billetes 5000 = 1')
elif monto == 70000:
  print('billetes 20000 = 3')
  print('billetes 10000 = 1')
  print('billetes 5000 = 0')
elif monto == 75000:
  print('billetes 20000 = 3')
  print('billetes 10000 = 1')
  print('billetes 5000 = 1')
elif monto == 80000:
  print('billetes 20000 = 4')
  print('billetes 10000 = 0')
  print('billetes 5000 = 0')
elif monto == 85000:
  print('billetes 20000 = 4')
  print('billetes 10000 = 0')
  print('billetes 5000 = 1')
elif monto == 90000:
  print('billetes 20000 = 4')
  print('billetes 10000 = 1')
  print('billetes 5000 = 0')
elif monto == 95000:
  print('billetes 20000 = 4')
  print('billetes 10000 = 1')
  print('billetes 5000 = 1')
elif monto == 100000:
  print('billetes 20000 = 5')
  print('billetes 10000 = 0')
  print('billetes 5000 = 0')
      