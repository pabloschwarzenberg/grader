#Cajero Automático
i=0
j='S'
g=0
cajero=1000000
cuenta=100000
div1=0
div2=0
div3=0
suma=0


def ResCaj(monto,cajero):
  cajero=cajero-monto
  return cajero

def ResCuenta(monto,cuenta):
  cuenta=abs(cuenta-monto)
  return cuenta

def BillVein(monto2,div1):
  div1=monto2//20000
  return div1

def BillDie(monto2,div2):
  div2=monto2//10000
  return div2

def BillCinc(monto2,div3):
  div3=monto2//5000
  return div3

usuario=eval(input('Ingrese usuario: '))
while usuario!=10334151:
  print('Usuario desconocido')
  usuario=eval(input('Ingrese usuario: '))
while i<=3 and usuario==10334151:
  if i==3:
    print('Tarjeta Bloqueada')
    break
  clave=eval(input('Ingrese Clave: '))
  if clave!=1803:
    i+=1
    print('clave invalida')
  if clave==1803:
    break
while clave==1803:
  if j!='S':
    break
  if j=='S':
    lista=['saldo cuenta= ','saldo cajero= ']
    lista2=['billetes 20000=','billetes 10000=','billetes 5000=']
    lista3=['suma de billetes= ']
    monto=eval(input('Ingrese Monto: '))
    if monto>cajero or monto>cuenta:
      print('No permitido')
      break
    if monto<=cajero:
      cajero=ResCaj(monto,cajero)
    if monto<=cuenta:
      cuenta=ResCuenta(cuenta,monto)
    monto2=monto
    if monto2//20000>=1:
      div1=BillVein(monto2,div1)
      monto2=monto2-(20000*div1)
    if monto2//10000>=1:
      div2=BillDie(monto2,div2)
      monto2=monto2-(10000*div2)
    if monto2//5000>=1:
      div3=BillCinc(monto2,div3)
      monto2=monto2-(5000*div3)
    lista[0]=lista[0]+str(cuenta)
    lista[1]=lista[1]+str(cajero)
    lista2[0]=lista2[0]+str(div1)
    lista2[1]=lista2[1]+str(div2)
    lista2[2]=lista2[2]+str(div3)
    suma+=monto
    lista3[0]=lista3[0]+str(suma)
    print('saldo cuenta= ',cuenta)
    print('saldo cajero= ',cajero)
    print('billetes 20000= ',div1)
    print('billetes 10000= ',div2)
    print('billetes 5000= ',div3)
    j=input('Desea repetir? (S/No): ')