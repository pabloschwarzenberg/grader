
saldoinicial = 1000000
saldoinicialcuenta = 100000 
user = int(input('Ingresa un usuario: ')) #10334151
while (user != 10334151):
    user = int(input('ERROR,Ingresa un usuario: '))
clave = int(input('Ingresa una clave para ingresar: ')) #1803
inte = 0
while (clave != 1803):
    inte = inte + 1
    if (inte == 3):
        print('Tarjeta bloqueda.')
        break
    else:
        clave = int(input('Clave inválida: ')) #1803
if inte != 3:
    montoretirar = int(input('Ingresa el monto a retirar: '))
if(montoretirar > 100000):
        montoretirar = int(input('Monto no permitido:'))

else:
    print('Saldo cuenta =', saldoinicialcuenta - montoretirar)
    print('Saldo cajero =', saldoinicial - montoretirar)
a = 0
b = 0
c = 0
while(montoretirar > 4000):
    if(montoretirar >= 20000):
        a = a + 1
        montoretirar = montoretirar - 20000
    elif(montoretirar >= 10000):
        b = b + 1
        montoretirar = montoretirar - 10000
    elif(montoretirar >= 5000):
        c = c + 1
        montoretirar = montoretirar - 5000

if(a!=0):
   print('Billetes 20000= ',a)
if(b!=0):
   print('Billetes 10000=', b)
if(c!=0):
   print('Billetes 5000=',c)