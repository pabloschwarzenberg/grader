#Cajero Automático
pres='N'
saldoCaj=1000000
saldoUs=100000
while(pres=='N'):
  sabeClave=False
  user=input('Ingrese usuario: ')
  while(user!='10334151'):
    user=input('Usuario erroneo, ingrese nuevamente: ')
  for i in range(3):
    clave=input('Ingrese clave: ')
    if(clave=='1803'):
      aRetirar=int(input('monto a retirar '))
      if(saldoUs>aRetirar and saldoCaj>aRetirar):
        saldoUs-=aRetirar
        print('saldo cuenta=',saldoUs)
        saldoCaj-=aRetirar
        print('saldo cajero=',saldoCaj)
        sabeClave=True
        break
      else:
        print('monto no permitido')
        sabeClave=True
        break
    else:
      print('clave invalida')
  if(not sabeClave):
    print('tarjeta bloqueada')
    break
  pres=input('presione cualquier tecla para salir. N para utilizar el cajero ')