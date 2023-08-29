#Cajero Automático
a=int(input('ingrese nombre de usuario:'))
b=int(input('ingrese clave:'))
contador=1
saldo_c=1000000
saldo_p=100000
while contador <= 3:
    if a==10334151 and b== 1803:
        x=int(input('ingrese monto a retirar:'))
        if x>=100000:
            print('monto no permitido')
        else:
            print('saldo cuenta=', saldo_p-x)
            print('saldo cajero=', saldo_c-x)
            break
    else:
        if contador==3:
            print('targeta bloqueada')
            break
        else:
            print('clave invalida')
            b=int(input('ingrese clave:'))
            contador+=1    