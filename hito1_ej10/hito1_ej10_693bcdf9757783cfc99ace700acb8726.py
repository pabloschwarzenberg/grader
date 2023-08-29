saldo_cajero = 1000000
clave_sec = 1803
intento = 3
clave_val = False
usuario = input('Ingrese su usuario: ')
while intento != 0 and not clave_val:
    clave = int(input('Ingrese su clave secreta: '))
    if clave//1000 < 1 or clave//1000 > 9:
        print('Ingrese clave de 4 digitos')
        continue
    if clave != clave_sec:
        print('clave invalida')
        intento -= 1
    else:
        print('Bienvenido', usuario)
        clave_val = True
        cuenta = 100000
        monto = int(input('Ingrese monto a retirar: '))
        if monto > cuenta:
            print('monto no permitido')
        else:
            cuenta -= monto
            saldo_cajero -= monto

if intento == 0:
    print('tarjeta bloqueada')
print('saldo cuenta=', cuenta)
print('saldo cajero=', saldo_cajero)

