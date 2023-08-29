#Cajero Automático
#Cajero Automático
i=0
j='S'
g=0
cajero=1000000
cuenta=100000
div1=0
div2=0
div3=0
#lista=['saldo cuenta= ','saldo cajero= ']


def ResCaj(monto,cajero):
  cajero=cajero-monto
  return cajero

def ResCuenta(monto,cuenta):
  cuenta=abs(cuenta-monto)
  return cuenta

def BillVein(cuenta2,div1):
  div1=cuenta2//20000
  return div1

def BillDie(cuenta2,div2):
  div2=cuenta2//10000
  return div2

def BillCinc(cuenta2,div3):
  div3=cuenta2//5000
  return div3

usuario=eval(input('Ingrese usuario: '))
if usuario!=10334151:
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
    print(lista,lista2)
    break
  if j=='S':
    lista=['saldo cuenta= ','saldo cajero= ']
    lista2=['billete 20000= ','billete 10000= ','billete 5000= ']
    monto=eval(input('Ingrese Monto: '))
    if monto>cajero or monto>cuenta:
      print('No permitido')
      break
    if monto<cajero:
      cajero=ResCaj(monto,cajero)
    if monto<cuenta:
      cuenta=ResCuenta(cuenta,monto)
    cuenta2=cuenta
    if cuenta2//20000>=1:
      div1=BillVein(cuenta2,div1)
      cuenta2=cuenta2-(20000*div1)
    if cuenta2//10000>=1:
      div2=BillDie(cuenta2,div2)
      cuenta2=cuenta2-(10000*div2)
    if cuenta2//5000>=1:
      div3=BillCinc(cuenta2,div3)
      cuenta2=cuenta2-(5000*div3)
    lista[0]=lista[0]+str(cuenta)
    lista[1]=lista[1]+str(cajero)
    lista2[0]=lista2[0]+str(div1)
    lista2[1]=lista2[1]+str(div2)
    lista2[2]=lista2[2]+str(div3)
    print(lista,lista2)
    j=input('Desea repetir? (S/No): ')