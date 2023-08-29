x='A'
saldocajero=1000000
saldocuenta=100000
usuario=int(input('Ingrese numero de usuario: '))
i=3
clave=int(input('Ingrese su clave: '))
while x != ('N'):
  if usuario==10334151 and clave==1803:
    monto=input('Ingrese monto a retirar: ')
    monto=float(monto)
    if monto>saldocuenta and monto>saldocajero:
      print('monto no permitido')
    else:
      saldocuenta=saldocuenta-monto
      saldocajero=saldocajero-monto
      print('[ saldo cuenta=', saldocuenta,',','saldo cajero=', saldocajero,']')
  else:
    print('clave invalida')
    i=i-1
    if i==0:
      print('tarjeta bloqueada')
      break