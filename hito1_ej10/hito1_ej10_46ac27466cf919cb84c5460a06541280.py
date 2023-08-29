#Cajero Automático
saldo_inicial = 1000000
saldo_ci = 100000
usuario = 10334151
clave = int(input('Ingrese clave: '))
intentos = 1
while True:
  if clave == 1803:
    monto = int(input('Que monto desea retirar? '))
    while monto > 100000:
      print('monto no permitido')
      monto = int(input('Que monto desea retirar? '))
    saldo_cajero = saldo_inicial - monto
    saldo_cuenta = saldo_ci - monto
    print('saldo cuenta=', saldo_cuenta,'\nsaldo cajero=', saldo_cajero)
    break
  elif intentos == 3:
    print('Tarjeta Bloqueada')
    break
  else: 
    print('clave invalida')
    clave = int(input('Ingrese clave: '))
    intentos += 1      