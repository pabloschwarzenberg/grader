#Cajero Automático
while True:
  usuario= float( input ( "ingrese un usuario de 7 digitos:"))
  clave= float (input ("ingrese una clave de 4 digitos:"))
  usu= 10334151
  cla= 1803
  retiro=0
  saldoinicial= 1000000
  saldocuenta=100000
  billete20=20
  billete10=40
  billet5=40
  billetesacado20=0
  billetesacado10=0
  billetesacado5=0
  if usuario == usu and clave== cla :
    #print ("cuanto monto desea retirar")
    retiro= int( input ( "ingrese el monto a retirar"))
    if retiro >= saldoinicial :
      print ("monto no permitidio")
    else:
      print ("saldo cuenta="+str(saldocuenta - retiro))
      print ("saldo cajero="+str(saldoinicial - retiro))
      if retiro>0:
        while retiro!=0:
          if retiro%20000==0:
            billetesacado20+=1
            retiro=retiro-20000
          elif retiro%10000==0:
            billetesacado10+=1     
            retiro=retiro-10000
          elif retiro%5000==0:
            retiro=retiro-5000
            billetesacado5+=1
        print('billetes 20000=',billetesacado20) 
        print('billetes 10000=',billetesacado10)
        print('billetes 5000=',billetesacado5)
  if usuario != usu or clave != cla :
    print ("clave invalida")
    usuario2= float( input ( "ingrese un usuario de 7 digitos:"))
    if usuario2!= usu or clave != cla :
      print ("clave ivalida")
    if usuario2 != usu or clave != cla :
      print ("tarjeta bloqueada")
  respuesta= input (" desea salir s o N")
  if respuesta != "N" :
    print ("buenas tardes")
    break
  if retiro>0:
    while retiro!=0:
      if retiro%20000==0:
        billetesacado20+=1
        retiro=retiro/20000
      elif retiro%10000==0:
        billetesacado10+=1     
        retiro=retiro/10000
      elif retiro%5000==0:
         billetesacado5+=1
    print('billetes 20000=',billetesacado20) 
    print('billetes 10000=',billetesacado10)
    print('billetes 5000=',billetesacado5) 

  
  
  
  
  
  
  