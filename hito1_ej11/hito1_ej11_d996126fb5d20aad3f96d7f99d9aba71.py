#Cajero Automático
SaldoCajero=1000000
SaldoUsuario=100000
usuario=10334151
clave=1803
i=0
UsuarioIngresado=int(input('Ingresa tu usuario: '))
ClaveIngresada=int(input('Ingresa tu clave: '))
       
if clave!=ClaveIngresada:
    while i<2:
        print('Clave Invalida')
        ClaveIngresada=int(input('Ingresa tu clave: '))
        i=i+1

if i==2:
    print('Tarjeta Bloqueada')

  
elif clave==ClaveIngresada:
   
        monto=int(input('Ingresa el monto a retirar: '))

        while monto>SaldoUsuario:
            print('Monto no permitido')
            monto=int(input('Ingresa el monto a retirar: '))
            
        print('Saldo cajero=',1000000-monto)
        print('Saldo cuenta=',100000-monto)      
 
BilletesDeVeinte=20
BilletesDeDiez=40
BilletesDeCincomil=40

a=monto//20000
if a>BilletesDeVeinte:
  a=BilletesDeVeinte
monto=monto-a*20000
BilletesDeVeinte=20-a
        
b=monto//10000
if b>BilletesDeDiez:
  b=BilletesDeDiez
monto=monto-b*10000
BilletesDeDiez=40-b

c=monto//5000
if c>BilletesDeCincomil:
  c=BilletesDeCincomil
monto=monto-c*5000
BilletesDeCincomil=40-c

print('billetes 20000 = ',a)
print('billetes 10000 = ',b)
print('billetes 5000 = ',c)
   
   