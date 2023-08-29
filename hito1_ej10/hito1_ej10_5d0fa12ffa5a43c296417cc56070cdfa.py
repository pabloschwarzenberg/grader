usua = int(input('ingrese su usuario: '))


saldoi = 1000000
saldoc = 100000
retiro = 1

intentos = 3
conteo = 1

while usua != 10334151:
    usua = int(input('Error usuario incorrecto, por favor ingrese su usuario: '))

clave = int(input('ingrese su clave: '))

while(intentos>conteo):
    if (clave != 1803):
        clave = int(input('Contraseña erronea, por favor ingrese su clave: '))
        conteo = conteo + 1

    else:
        retiro = int(input('Ingrese el monto a retirar: '))
        break

if(saldoi>=retiro):
    restoi = saldoi-retiro
    restoc = saldoc-retiro
    print('saldo cuenta='+str(restoc))
    print('saldo cajero='+str(restoi))

if(conteo==3):
    a = 'tarjeta bloqueada'
    print(a)