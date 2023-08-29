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
       
      