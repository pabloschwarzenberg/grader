#Cajero Automático
dinero_caj=1000000
b_20k=20
b_10k=40
b_5k=50
usuario=int(input("introduzca su numero de usuario:"))
contrasena=int(input("introduzca su contrasena secreta:"))
i=0
while usuario!=10334151 and contrasena!=1803:
  i=i+1
  user_2=int(input("ingrese nuevamente su usuario porfavor:"))
  contra=int(input("ingrese nuevamente su clave porfavor:"))
  if i>3:
    print("TARJETA BLOQUEADA")
    break
if usuario==10334151 and contrasena==1803:
  saldo_inicialcuenta=100000
  ret=int(input("ingrese el monto a retirar porfavor:"))
  if ret<0 or ret>100000:
    print("MONTO INVALIDO")
  else:
    din_cajrest=dinero_caj - ret
    dinero_cuenta=saldo_inicialcuenta - ret
    ret_20k=ret//20000
    ret_10k=(ret - ret_20k*20000)//10000
    ret_5k=(ret - ret_20k*20000 - ret_10k*10000)//50000
    b_20k=b_20k - ret_20k
    b_10k=b_10k - ret_10k
    b_5k=b_5k - ret_5k
    print("billetes 20000= "+str(ret_20k))
    print("billetes 10000= "+str(ret_10k))
    print("billetes 5000= "+str(ret_5k))
    print("saldo cuenta= "+str(dinero_cuenta))
    print("saldo cajero= "+str(din_cajrest))