#Cajero Automático
usuario=int(input("Ingrese usuario: ")) 
while usuario==10334151:
  codigo=1803
  saldoCuentaI=100000
  saldoCajeroI=1000000
  errores=0
  montoRetira=int(input("ingrese monto de retiro: "))
  if montoRetira>saldoCuentaI:
    print("monto no permitido")
    montoRetira=int(input("ingrese monto de retiro: "))
    
  contrasenia=int(input("Confirme con contraseña: "))  

  elif contrasenia==codigo:
    saldocuenta=saldoCuentaI-montoRetira
    saldoCuentaI=saldocuenta
    print(saldocuenta)
    saldocajero=saldoCajeroI-montoRetira
    saldoCajeroI=saldocajero
    print(saldocajero)
    exit()
  else:
    print("clave invalida")
    errores+=1
    contrasenia=int(input("Confirme con contraseña: "))
    if errores==3:
        print("tarjeta bloqueada")
        exit()