#Cajero Automático
Y="N"
saldo_cajero=1000000
intentos=0
while intentos<3 :
  intentos=intentos+1
  usuario=eval(input("Ingrese su código de usuario"))
  clave=eval(input("Ingrese clave"))
  if usuario==10334151 and clave==1803:
    print("Bienvenido usuario ", usuario)
    saldo_usuario=100000
    retiro=int(input("Ingrese monto a retirar"))
    if retiro < saldo_usuario and retiro>0:
      saldo_usuario=saldo_usuario - retiro
      print("saldo cuenta=",saldo_usuario)
      saldo_cajero=saldo_cajero - retiro
      print("saldo cajero=",saldo_cajero)
    if retiro > saldo_usuario:
      print("monto no permitido")
  else: #if clave != 1803:
    print("clave invalida")
    print ("intentos:",intentos)
    if intentos ==3:
      print("clave bloqueada")
      break