saldo=1000000
cuenta=100000
usuario=10334151
clave=1803
c=int(input('ingrese clave numerica:'))
i=0
while i<3:
  if c!=clave:
    c=int(input('clave invalida, intente de nuevo'))
  else:
    break
  i+=1
if c==clave:
  salir='n'
  while salir!='y':
    monto=int(input('ingrese monto a retirar:'))
    if monto>cuenta:
      print('monto no permitido')
    else:
      saldo-=monto
      cuenta-=monto
      print('saldo cuenta=',cuenta)
      print('saldo cajero=',saldo)
    salir=input('desea salir(n=no, y=si)')
    salir=salir.lower()
elif i==3:
  print('tarjeta bloqueada')