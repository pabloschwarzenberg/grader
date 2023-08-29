#Cajero Automático
usuario=int(input("ingrese su nombre de usuario: "))
clave=int(input("ingrese su clave: "))
saldo_inicial=1000000
if usuario==10334151 and clave==1803:
  saldo_cuenta=100000
  print('saldo cuenta:',saldo_cuenta)
  retirar_dinero=int(input("cuando dinero desea retirar de su cuenta corriente?: "))
  saldo_restante=saldo_cuenta - retirar_dinero
  print('saldo cuenta:',saldo_restante)
  saldo_cuentafinal=saldo_cuenta - retirar_dinero
  saldo_inicialfinal=saldo_inicial - retirar_dinero
  print('saldo cuenta=',saldo_cuentafinal)
  print('saldo cajero=',saldo_inicialfinal)
  if retirar_dinero>saldo_restante:
    print("monto no permitido")
else:
  print("usuario incorrecto")
  i=0
  while i<4 and usuario!=10334151 and clave!=1803:
    i=i+1
    usuario2=int(input("ingrese nuevamente su nombre de usuario: "))
    contra=int(input("ingrese nuevamente su contraseña: "))
    if i>2 and contra!=1803 and usuario2!=10334151:
      print("TARJETA BLOQUEADA")
      break
    if usuario2==10334151 and contra==1803:
     dinero_cuenta=100000
     dinero_cajero=1000000
     dinero_cuenta2=str(int(dinero_cuenta))
     print("BIENVENIDO, SU DINERO FINAL EN EL CAJERO ES DE: ",dinero_cajero,"Y SU DINERO EN LA CUENTA ES DE" +str(dinero_cuenta))
     ret_cuentacor=int(input("Cuanto dinero desea retirar de su cuenta?: "))
     dinero_cuentatotal=dinero_cuenta - ret_cuentacor
     print("SALDO CUENTA=:",dinero_cuentatotal)
     dinero_cajerototal=dinero_cajero - ret_cuentacor
     print("Saldo CAJERO=:",dinero_cajerototal)
     if ret_cuentacor>dinero_cuenta or ret_cuentacor>dinero_cajero:
       print("MONTO NO PERMITIDO")
     break



