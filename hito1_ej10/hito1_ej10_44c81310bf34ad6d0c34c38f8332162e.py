#Cajero Automático
print('#usuario 10334151')

intentos=1
clave=1803
cajeroinicio=1000000
saldoinicio=100000

while intentos <=3:
    password=int(input('Ingrese su clave:'))
    intentos=intentos+1

    if intentos>3:
        print('Tarjeta Bloqueada')
        break

    if password==clave:
        monto=int(input('Ingrese monto a retirar:'))
        while monto:
            if 0<monto<=100000:
                finalcuenta=(saldoinicio-monto)
                finalcajero=(cajeroinicio-monto)
                print('saldo cuenta=',finalcuenta)
                print('saldo cajero=',finalcajero)
                break
            else:
                print('monto no permitido')
        break