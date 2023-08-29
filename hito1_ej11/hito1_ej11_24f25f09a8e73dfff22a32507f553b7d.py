#Cajero automÃ¡tico
cajero=1000000
intentos=0
intentosc=0
sesionc=0
sesion=0
saldo=100000
#Billetes:
b20=20
b10=40
b5=40
b20u=0
b10u=0
b5u=0


#Funciones
def user(x):
  if x == 10334151:
    return True
  else:
    return False

def pw(y):
  if y == 1803:
    return True
  else:
    return False
  
#Programa 
#*Iniciar:
while intentos<3 and sesion==0:
  us=int(input("Ingrese usuario >"))
  p=int(input("Ingrese clave >"))
  if user(us)==True and pw(p)==True:
   sesion=1
   print("Sesion iniciada")
  elif user(us)==True and pw(p)==False:
    print("clave invalida")
    intentos=intentos+1
    print("Intentos restantes:",3-intentos)
  elif user(us)==False and pw(p)==True:
    print("usuario invalido")
    intentos=intentos+1
    print("Intentos restantes:",3-intentos)
if intentos>=3:
  print("tarjeta bloqueada")
#Ingesado al cajero
while sesion==1:
  retiro=int(input("monto a retirar >:$"))
  if retiro <= cajero and retiro <= saldo:
    print("saldo cuenta=",saldo-retiro)
    print("saldo cajero=",cajero-retiro)
    cajero=cajero-retiro
    saldo=saldo-retiro
    if retiro/(20000) >= 1 :
     b20u=int(retiro/(b20*1000))
     retiro=retiro-(20000*b20u)
     
  
   
    if retiro/(10000) >= 1 :
     b10u=int(retiro/(10000)) 
     retiro=retiro-(10000*b10u)
     
   
    if retiro/(5000) >= 1 :
     b5u=int(retiro/(5000))
     retiro=retiro-(5000*b5u)
  print("billetes 20000=",b20u)
  print("billetes 10000=",b10u)
  print("billetes 5000=",b5u)

  sesion=0
