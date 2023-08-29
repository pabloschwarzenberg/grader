#Cajero Automático
i=0
j='S'
g=0
cajero=1000000
cuenta=100000

def ResCaj(monto,cajero):
  cajero=cajero-monto
  return cajero

def ResCuenta(monto,cuenta):
  cuenta=abs(cuenta-monto)
  return cuenta

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
    print(lista)
    break
  if j=='S':
    lista=['saldo cuenta= ','saldo cajero= ']
    monto=eval(input('Ingrese Monto: '))
    if monto>cajero or monto>cuenta:
      print('No permitido')
      break
    if monto<cajero:
      cajero=ResCaj(monto,cajero)
    if monto<cuenta:
      cuenta=ResCuenta(cuenta,monto)
    lista[0]=lista[0]+str(cuenta)
    lista[1]=lista[1]+str(cajero)
    print(lista)
    j=input('Desea repetir? (S/No): ')