#Cajero automático
cajero=1000000
intentos=0
intentosc=0
sesionc=0
sesion=0
saldo=100000
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
    sesion=0