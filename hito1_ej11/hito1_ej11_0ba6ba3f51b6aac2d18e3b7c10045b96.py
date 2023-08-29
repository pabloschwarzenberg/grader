#Cajero Automático
inicio=1000000
saldo=100000
y=1
x=0
a=""
B20=20
B10=40
B5=40
nombre=int(input('ingrese usario:'))
x=int(input('ingrese clave:'))
while (a!=1):
     if x!=1803:
          x=int(input('ingrese clave nuevamente:'))
          y=y+1
          if x!=1803:
               x=int(input('ingrese clave nuevamente:'))
               y=y+1
               if x!=1803:
                    print('tarjeta bloqueada!')
               elif x==1803:
                    j=int(input('¡cuanto desea retirar? (solo montos multiplos de 5000):'))
                    c=j//10000
                    b=j%10000
                    if inicio<j or saldo<j:
                         print('monto no permitido, intente nuevamente')
                    else:
                         if j==5000:
                              print('-')
                              print('Billetes 5000=1')
                              print('-')
                         elif j==10000:
                              print('-')
                              print('Billetes 10000=1')
                              print('-')
                         elif c==1 and b==5000:
                              print('-')
                              print('Billetes 10000=1')
                              print('Billetes 5000=1')
                              print('-')
                         elif c==2 and b!=5000:
                              print('-')
                              print('Billetes 20000=1')
                              print('-')
                         elif c==2 and b==5000:
                              print('-')
                              print('Billetes 20000=1')
                              print('Billetes 5000=1')
                              print('-')
                         elif c==3 and b!=5000:
                              print('-')
                              print('Billetes 20000=1')
                              print('Billete 10000=1')                         
                              print('-')
                         elif c==3 and b==5000:
                              print('-')
                              print('Billetes 20000=1')
                              print('Billetes 10000=1')
                              print('Billetes 5000=1')
                              print('-')
                         elif c==4 and b!=5000:
                              print('-')
                              print('Billetes 20000=2')
                              print('-')
                         elif c==4 and b==5000:
                              print('-')
                              print('Billetes 20000=2')
                              print('Billetes 5000=1')
                              print('-')
                         elif c==5 and b!=5000:
                              print('-')
                              print('Billetes 20000=2')
                              print('Billetes 10000=1')
                              print('-')
                         elif c==5 and b==5000:
                              print('-')
                              print('Billetes 20000=2')
                              print('Billetes 10000=1')
                              print('Billetes 5000=1')
                              print('-')
                         elif c==6 and b!=5000:
                              print('-')
                              print('Billetes 20000=3')
                              print('-')
                         elif c==6 and b==5000:
                              print('-')
                              print('Billetes 20000=3')
                              print('Billetes 5000=1')
                              print('-')
                         elif c==7 and b!=5000:
                              print('-')
                              print('Billetes 20000=2')
                              print('Billetes 10000=3')
                              print('-')
                         elif c==7 and b==5000:
                              print('-')
                              print('Billetes 20000=2')
                              print('Billetes 10000=3')
                              print('Billetes 5000=1')
                         elif c==8 and b!=5000:
                              print('-')
                              print('Billetes 20000=4')
                              print('-')
                         elif c==8 and b==5000:
                              print('-')
                              print('Billetes 20000=4')
                              print('Billetes 5000=1')
                              print('-')
                         elif c==9 and b!=5000:
                              print('-')
                              print('Billetes 20000=4')
                              print('Billetes 10000=1')
                              print('-')
                         elif c==9 and b==5000:
                              print('-')
                              print('Billetes 20000=4')
                              print('Billetes 10000=4')
                              print('Billetes 5000=1')
                              print('-')
                         elif c==10 and b!=5000:
                              print('-')
                              print('Billetes 20000=5')
                              print('-')
                         inicio=inicio-j
                         saldo=saldo-j
                         print('saldo cuenta=',saldo)
                         print('saldo cajero=',inicio)
                         print('-')
                         a=input('¿Desea Salir?,Digite 1 para salir:')
          elif x==1803:
               j=int(input('¿cuanto desea retirar?:'))
               c=j//10000
               b=j%10000
               if inicio<j or saldo<j:
                    print('monto no permitido, intente nuevamente')
               else:
                    if j==5000:
                         print('-')
                         print('Billetes 5000=1')
                         print('-')
                    elif j==10000:
                         print('-')
                         print('Billetes 10000=1')
                         print('-')
                    elif c==1 and b==5000:
                         print('-')
                         print('Billetes 10000=1')
                         print('Billetes 5000=1')
                         print('-')
                    elif c==2 and b!=5000:
                         print('-')
                         print('Billetes 20000=1')
                         print('-')
                    elif c==2 and b==5000:
                         print('-')
                         print('Billetes 20000=1')
                         print('Billetes 5000=1')
                         print('-')
                    elif c==3 and b!=5000:
                         print('-')
                         print('Billetes 20000=1')
                         print('Billete 10000=1')                         
                         print('-')
                    elif c==3 and b==5000:
                         print('-')
                         print('Billetes 20000=1')
                         print('Billetes 10000=1')
                         print('Billetes 5000=1')
                         print('-')
                    elif c==4 and b!=5000:
                         print('-')
                         print('Billetes 20000=2')
                         print('-')
                    elif c==4 and b==5000:
                         print('-')
                         print('Billetes 20000=2')
                         print('Billetes 5000=1')
                         print('-')
                    elif c==5 and b!=5000:
                         print('-')
                         print('Billetes 20000=2')
                         print('Billetes 10000=1')
                         print('-')
                    elif c==5 and b==5000:
                         print('-')
                         print('Billetes 20000=2')
                         print('Billetes 10000=1')
                         print('Billetes 5000=1')
                         print('-')
                    elif c==6 and b!=5000:
                         print('-')
                         print('Billetes 20000=3')
                         print('-')
                    elif c==6 and b==5000:
                         print('-')
                         print('Billetes 20000=3')
                         print('Billetes 5000=1')
                         print('-')
                    elif c==7 and b!=5000:
                         print('-')
                         print('Billetes 20000=2')
                         print('Billetes 10000=3')
                         print('-')
                    elif c==7 and b==5000:
                         print('-')
                         print('Billetes 20000=2')
                         print('Billetes 10000=3')
                         print('Billetes 5000=1')
                    elif c==8 and b!=5000:
                         print('-')
                         print('Billetes 20000=4')
                         print('-')
                    elif c==8 and b==5000:
                         print('-')
                         print('Billetes 20000=4')
                         print('Billetes 5000=1')
                         print('-')
                    elif c==9 and b!=5000:
                         print('-')
                         print('Billetes 20000=4')
                         print('Billetes 10000=1')
                         print('-')
                    elif c==9 and b==5000:
                         print('-')
                         print('Billetes 20000=4')
                         print('Billetes 10000=4')
                         print('Billetes 5000=1')
                         print('-')
                    elif c==10 and b!=5000:
                         print('-')
                         print('Billetes 20000=5')
                         print('-')
                    inicio=inicio-j
                    saldo=saldo-j
                    print('saldo cuenta=',saldo)
                    print('saldo cajero=',inicio)
                    print('-')
                    a=input('¿Desea Salir?,Digite 1 para salir:')                    
     elif x==1803:
          j=int(input('¿cuanto desea retirar?:'))
          c=j//10000
          b=j%10000
          if inicio<j or saldo<j:
               print('monto no permitido, intente nuevamente')
          else:
               if j==5000:
                    print('-')
                    print('Billetes 5000=1')
                    print('-')
               elif j==10000:
                    print('-')
                    print('Billetes 10000=1')
                    print('-')
               elif c==1 and b==5000:
                    print('-')
                    print('Billetes 10000=1')
                    print('Billetes 5000=1')
                    print('-')
               elif c==2 and b!=5000:
                    print('-')
                    print('Billetes 20000=1')
                    print('-')
               elif c==2 and b==5000:
                    print('-')
                    print('Billetes 20000=1')
                    print('Billetes 5000=1')
                    print('-')
               elif c==3 and b!=5000:
                    print('-')
                    print('Billetes 20000=1')
                    print('Billete 10000=1')                         
                    print('-')
               elif c==3 and b==5000:
                    print('-')
                    print('Billetes 20000=1')
                    print('Billetes 10000=1')
                    print('Billetes 5000=1')
                    print('-')
               elif c==4 and b!=5000:
                    print('-')
                    print('Billetes 20000=2')
                    print('-')
               elif c==4 and b==5000:
                    print('-')
                    print('Billetes 20000=2')
                    print('Billetes 5000=1')
                    print('-')
               elif c==5 and b!=5000:
                    print('-')
                    print('Billetes 20000=2')
                    print('Billetes 10000=1')
                    print('-')
               elif c==5 and b==5000:
                    print('-')
                    print('Billetes 20000=2')
                    print('Billetes 10000=1')
                    print('Billetes 5000=1')
                    print('-')
               elif c==6 and b!=5000:
                    print('-')
                    print('Billetes 20000=3')
                    print('-')
               elif c==6 and b==5000:
                    print('-')
                    print('Billetes 20000=3')
                    print('Billetes 5000=1')
                    print('-')
               elif c==7 and b!=5000:
                    print('-')
                    print('Billetes 20000=2')
                    print('Billetes 10000=3')
                    print('-')
               elif c==7 and b==5000:
                    print('-')
                    print('Billetes 20000=2')
                    print('Billetes 10000=3')
                    print('Billetes 5000=1')
                    print('-')
               elif c==8 and b!=5000:
                    print('-')
                    print('Billetes 20000=4')
                    print('-')
               elif c==8 and b==5000:
                    print('-')
                    print('Billetes 20000=4')
                    print('Billetes 5000=1')
                    print('-')
               elif c==9 and b!=5000:
                    print('-')
                    print('Billetes 20000=4')
                    print('Billetes 10000=1')
                    print('-')
               elif c==9 and b==5000:
                    print('-')
                    print('Billetes 20000=4')
                    print('Billetes 10000=4')
                    print('Billetes 5000=1')
                    print('-')
               elif c==10 and b!=5000:
                    print('-')
                    print('Billetes 20000=5')
                    print('-')
          inicio=inicio-j
          saldo=saldo-j
          print('saldo cuenta=',saldo)
          print('saldo cajero=',inicio)
          print('-')
          a=input('¿Desea Salir?,Digite "1" para salir:')
print('Hasta Luego')
      