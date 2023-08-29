#cajero automatico
salir="N"
while salir=="N":
    intentos= 3
    usuario=float(input("ingrese usuario"))
    while intentos>0:
        
      clave=float(input("ingrese clave"))
      if usuario==float(10334151) and clave==float(1803):
          print("usuario permitido")
          break

      elif clave!=float(1803) or usuario!=float(10334151):
          intentos=intentos-1
          print("clave invalida")
    if    intentos==0:
          print("tarjeta bloqueda")
    else:
     saldo_inicial_cajero=1000000
     saldo_usuario=100000
     monto_a_retirar=float(input("ingrese monto a retirar"))
    if monto_a_retirar<1000000 and monto_a_retirar<100000:
        saldo_inicial_cajero=saldo_inicial_cajero-monto_a_retirar
        saldo_usuario=saldo_usuario-monto_a_retirar
        print ("saldo cuenta=",saldo_usuario)
        print("saldo cajero=",saldo_inicial_cajero)
    salir=input("quieres salir")
     
