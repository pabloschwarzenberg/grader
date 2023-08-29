#Cajero Automático
cajero = 1000000
cuenta = 100000
usuario = 10334151
contraseña = 1803
billetes20 = 20
billetes10 = 40
billetes5 = 40
continua = True
while True:
    us = int(input('ingrese numero de usuario: '))
    if us != usuario:
        print('usuario incorrecto')
    elif us == usuario:
      contra = int(input('ingrese clave: '))
      if contra != 1803:
        print('intente nuevamente')
        contra = int(input('ingrese clave: '))
        if contra != 1803:
          print('intente nuevamente')
          contra = int(input('ingrese clave: '))
          if contra != 1803:
                    print('Tarjeta bloqueada')
                    break
      elif contra == 1803:
        monto = int(input('ingrese monto a retirar'))
        if monto>cuenta:
            print('monto no permitido')
        elif monto < 0:
            print('monto no permitido')
        else: 
             cajero = cajero-monto
             cuenta = cuenta - monto
             billetes_20 = monto/20000
             billetes_10 = (monto- 20000*(int(billetes_20)))/10000
             billetes_5 = (monto- 20000*(int(billetes_20))-10000*(int(billetes_10)))/5000 
             print('saldo cajero = ',cajero)
             print('saldo cuenta = ',cuenta)
             print('billetes 20000 = ',int(billetes_20))
             print('billetes 10000 = ',int(billetes_10))
             print('billetes 5000 = ',int(billetes_5))
             otro= input('desea hacer otro retiro(N: si): ')
             if otro != 'N':
                break
            
             