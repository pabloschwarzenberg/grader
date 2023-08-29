#Cajero Automático
cajero = 1000000
usuario = 10334151
contraseña = 1803
cajero = 1000000
cuenta = 100000
usuario = 10334151
contraseña = 1803
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
             print('saldo cuenta=', cuenta)
             print('saldo cajero=', cajero)
             otro= input('desea hacer otro retiro(N: si): ')
             if otro != 'N':
                break
              