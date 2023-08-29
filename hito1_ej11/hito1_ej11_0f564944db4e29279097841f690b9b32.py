#Cajero Automático
monto_cajero=1000000
monto_usuario=100000
clave_invalida=0
billetes_veinte=20
billetes_diez=40
billetes_cinco=40
while True:
    usuario=int(input('Ingrese numero de Usuario:'))
    clave=int(input('Ingrese Clave:'))
    if clave==1803 and usuario==10334151:
        monto_retirar=int(input('Ingrese monto a retirar:'))
        if monto_retirar<=100000:
            a=monto_retirar//100000
            print(a)
            b=monto_retirar%100000
            print(b)
            b=b//10000
            print(b)
            c=monto_retirar%10000
            print(c)
            c=c//1000
            print(c)
            if monto_usuario>=monto_retirar and monto_usuario>0:
                print('Se retira:',monto_retirar)
                monto_cajero=monto_cajero-monto_retirar
                monto_usuario=monto_usuario-monto_retirar
                print('saldo cuenta=',monto_usuario)
                print('saldo cajero=',monto_cajero)
                if a==1:
                    print('billetes 20000=',5)
                    print('billetes de 10000=',0)
                    print('billetes 5000=',0)
                elif a==0 and b%2==0 and c==5:
                    print('billetes 20000=',b//2)
                    print('billetes 10000=',0)
                    print('billetes 5000=',1)
                elif a==0 and b%2==0 and c==0:
                    print('billetes 20000=',b//2)
                    print('billetes 10000=',0)
                    print('billetes 5000=',0)
                elif a==0 and b%2!=0:
                    print('billetes 20000=',0)
                    print('billetes 10000=',b)
                    print('billetes 5000=',0)
                elif a==0 and b%2!=0 and c==5:
                    print('billetes 20000=',0)
                    print('billetes 10000=',b)
                    print('billetes 5000=',1)
                    
                salir=input('Desea salir(Digite N para continuar):')
                salir=salir.upper()
                if salir=="N":
                    continue
                else:
                    break
            else:
                print('No hay saldo suficiente')     
        else:
            print('monto no permitido')
    elif clave!=1803:
        print('clave invalida')
        clave_invalida=clave_invalida+1
        if clave_invalida==3:
            print('tarjeta bloqueada')
            break
        else:
            continue
    else:
        break

     