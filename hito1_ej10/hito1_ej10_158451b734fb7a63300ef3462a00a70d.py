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