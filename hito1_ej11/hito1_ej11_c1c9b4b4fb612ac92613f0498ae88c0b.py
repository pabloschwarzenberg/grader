saldo=1000000
bill20=20
bill10=40
bill5=40
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
      suma=0
      usado20=(monto//20000)
      suma+=(usado20*20000)
      mon=(monto%20000)
      usado10=(mon//10000)
      suma+=(usado10*10000)
      mon=(mon%10000)
      usado5=(mon//5000)
      suma+=(usado5*5000)
      mon=(mon%5000)
      print('saldo cuenta=',cuenta)
      print('saldo cajero=',saldo)
      print('billetes de 5.000=',usado5)
      print('billetes de 10.000=',usado10)
      print('billetes de 20.000=',usado20)
    salir=input('desea salir(n=no, y=si)')
    salir=salir.lower()
elif i==3:
  print('tarjeta bloqueada')