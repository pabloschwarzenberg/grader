#Cajero Automático
n = 0
validadorusuario = 10334151
validadorcontra = 1803
saldocajero = 1000000
saldocuenta = 100000
billete20 = 20
billete10 = 40
billete5 = 40
cont20,cont10,cont5=0,0,0
usuario = eval(input('usuario: '))
while True:
  contra = eval(input('contraseña: '))
  if contra != validadorcontra:
    print('clave invalida')
    n+=1
  else:break
  if n == 3:
    print('tarjeta bloqueda')
    break
while True:
  if n ==3:
    break
  monto = eval(input('monto a retirar: '))
  if monto > saldocajero:
    print('Monto no permitido')
  else:
    saldocajero = saldocajero - monto
    saldocuenta = saldocuenta - monto
    while monto>0:
      if monto>20000:
        monto = monto - 20000
        cont20 +=1
      elif monto > 10000 and monto<20000:
        monto = monto - 10000
        cont10 +=1
      elif monto<10000:
        monto = monto - 5000
        cont5 +=1
    print('billetes 20000=',cont20)
    print('billetes 10000=',cont10)
    print('billetes 5000=',cont5)
    print('saldo cuenta=',saldocuenta)
    print('saldo cajero=',saldocajero)
    break