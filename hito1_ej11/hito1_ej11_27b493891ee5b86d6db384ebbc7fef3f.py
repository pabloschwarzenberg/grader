#Cajero Automático
usuario = int(input("Ingrese su usuario: "))
clave = int(input("Ingrese su clave: "))
cajero = 1000000
cuenta = 100000
intento = 0
b20 = 20000*1
b10 = 10000*1
b5 = 5000*1
suma = 0
if usuario == 10334151:
 while intento < 2:
  if clave != 1803:
   intento = intento + 1
   print("clave invalida")
   clave = int(input("Ingrese su clave: "))
  if clave == 1803:
   print("clave valida")
   break
 else:
  print("tarjeta bloqueada")
  exit()

while usuario == 10334151 and clave == 1803:
  retiro = int(input("Monto a retirar: "))
  cuenta = 100000 - retiro
  if cuenta < 0:
   print("monto no permitido")
   retiro = int(input("Monto a retirar: "))
   cuenta = 100000 - retiro
  else:
   b20 = retiro // 20000
   resto20 = retiro % 20000
   b10 = resto20 // 10000
   resto10 = resto20 % 10000
   b5 = resto10 // 5000
   resto5 = resto10 % 5000
   print("saldo cuenta=",cuenta,",saldo cajero=",cajero - retiro)
   print("billetes 20000=",b20)
   print("billetes 10000=",b10)
   print("billetes 5000=",b5)
   break