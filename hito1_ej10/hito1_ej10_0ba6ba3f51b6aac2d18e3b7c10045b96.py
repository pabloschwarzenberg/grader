#Cajero Automático
nombre=int(input('ingrese usario:'))
inicio=1000000
saldo=100000
y=1
x=0
x=int(input('ingrese clave:'))
if x!=1803:
     x=int(input('ingrese clave nuevamente:'))
     y=y+1
     if x!=1803:
          x=int(input('ingrese clave nuevamente:'))
          y=y+1
          if x!=1803:
               print('tarjeta bloqueada!')
elif x==1803:
     j=int(input('cuanto desea retirar:'))
     if inicio<j or saldo<j:
          print('monto no permitido')
     else:
          inicio=inicio-j
          saldo=saldo-j
          print('saldo cuenta=',saldo)
          print('saldo cajero=',inicio)
               
          
      