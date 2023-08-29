#Cajero Automático
pres='N'
billetes=[20,40,40]

def cuentaBilletes(arreglo):
  return(20000*arreglo[0]+10000*arreglo[1]+5000*arreglo[2])

def particion(monto, arreglo):
  mAux=monto
  arrAux=[i for i in arreglo]
  while(mAux>0):
    if(mAux>=20000 and arrAux[0]>0):
      mAux-=20000
      arrAux[0]-=1
    elif(mAux>=10000 and arrAux[1]>0):
      mAux-=10000
      arrAux[1]-=1
    elif(mAux>=5000 and arrAux[2]>0):
      mAux-=5000
      arrAux[2]-=1
    else:
      print('Error')
      break
  return [arreglo[i]-arrAux[i] for i in range(len(arreglo))]




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
      billetesRetirar=particion(aRetirar,billetes)
      if(saldoUs>aRetirar and cuentaBilletes(billetes)>aRetirar):
        billetes[0]-=billetesRetirar[0]
        billetes[2]-=billetesRetirar[2]
        billetes[1]-=billetesRetirar[1]
        saldoUs-=aRetirar
        print('saldo cuenta=',saldoUs)
        print('saldo cajero=',cuentaBilletes(billetes))
        print('billetes 20000=',billetesRetirar[0])
        print('billetes 10000=',billetesRetirar[1])
        print('billetes 5000=',billetesRetirar[2])
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