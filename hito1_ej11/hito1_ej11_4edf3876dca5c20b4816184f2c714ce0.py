#Cajero Automático
#Cajero Automático
saldocajero = 1000000
saldocuenta = 100000
claveinvalida = 0

#usuario
nombreusuario = int(input('digite su numero: '))

while  claveinvalida <= 2:
    clave = int(input('digite su clave: '))
    if nombreusuario == 10334151 and clave == 1803:
        saldoretirar = int(input('que monto desea retirar: '))
        if saldoretirar > saldocuenta:
            print('monto no permitido')
            break
        saldocuenta = saldocuenta - saldoretirar
        saldocajero = saldocajero - saldoretirar
        print ('saldo cuenta=',saldocuenta)            
        print ('saldo cajero=',saldocajero)
        break
    else:
        print('clave invalida')
        claveinvalida = claveinvalida + 1        
        
if claveinvalida == 3:
    print('tarjeta bloqueada')