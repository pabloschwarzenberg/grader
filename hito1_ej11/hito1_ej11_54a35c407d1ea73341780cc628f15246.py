#Cajero Automático
inicio='N'
while inicio=='N':
    usuario=int(input('ingresse su cuenta:: '))
    clave=int(input('ingrse su clave: '))
    claveC=1803
    saldoC=1000000
    saldoU=100000
    billetes20=20000
    billetes10=10000
    billetes5=5000
    i=1
    while i<=2:
       if clave==claveC:
           break
       else:
           print('clave invalida')
           clave=int(input('ingrse su clave: '))
       i=i+1
    if i==3:
        print('tarjeta bloqueada')
        inicio=0
    else:
        monto=int(input('ingrese el monto a retirar: '))
        if monto>saldoC or monto>saldoU:
            print('monto invalido')
        else:
            saldoC=saldoC-monto
            saldoU=saldoU-monto
            cb20=monto//billetes20
            monto=monto-(billetes20*cb20)
            cb10=monto//billetes10
            monto=monto-(billetes10*cb10)
            cb5=monto//billetes5
            print('saldo cuenta=',saldoU)
            print('saldo cajero=',saldoC)
            print('billetes 20000=',cb20)
            print('billetes 10000=',cb10)
            print('billetes 5000=',cb5)
    inicio=input('terminar operacion? (seleccione N si desea continiuar): ')
    inicio.upper()
print('ha finalizado, gracias por preferirnos')      