usua = int(input('ingrese su usuario: '))


saldoi = 1000000
lukas20 = 20
lukas10 = 40
lukas5 = 40
saldoc = 100000
retiro = 1

a = 0
b = 0
c = 0

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

cambio = retiro

while(cambio>0):

    if(cambio>=20000):
        a = a+1
        cambio = cambio-20000

    if(cambio>=10000):
        b = b+1
        cambio = cambio-10000

    if(cambio>=5000):
        c = c+1
        cambio = cambio-5000

if(saldoi>=retiro):
    restoi = saldoi-retiro
    restoc = saldoc-retiro
    print('saldo cuenta='+str(restoc))
    print('saldo cajero='+str(restoi))
    print('billetes 20000='+str(a))
    print('billetes 10000='+str(b))
    print('billetes 5000='+str(c))

if(conteo==3):
    g = 'tarjeta bloqueada'
    print(g)