#Cajero Automático
usuario= float( input ( "ingrese un usuario de 7 digitos:"))
clave= float (input ("ingrese una clave de 4 digitos:"))
usu= 10334151
cla= 1803
retiro=0
saldoinicial= 1000000
saldocuenta=100000

if usuario == usu and clave== cla :
    #print ("cuanto monto desea retirar")
    retiro= int( input ( "ingrese el monto a retirar"))
    if retiro >= saldoinicial :
      print ("monto no permitidio")
    else:
      print ("saldo cuenta="+str(saldocuenta - retiro))
      print ("saldo cajero="+str(saldoinicial - retiro))
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
      