#ENTRADA
def amigos(x,y):
  divnumero1=1
  divnumero2=1
  sumanumero1=0
  sumanumero2=0

#DESARROLLO
  while divnumero1<x:
    if x%divnumero1==0:
      sumanumero1+=divnumero1
      print("divisor de %d es: %d" % (x,divnumero1),"la suma de divisores de %d es: %d" %(x,sumanumero1))
    divnumero1+=1
  while divnumero2<y:
    if y%divnumero2==0:
      sumanumero2+=divnumero2
      print("divisor de %d es: %d" % (y,divnumero2),"la suma de divisores de %d es: %d" %(y,sumanumero2))
    divnumero2 += 1
#SALIDA
  if sumanumero1==y and sumanumero2==x:
    return True
  else:
    return False
try:
 numero1 = int(input("Número 1: "))
 numero2 = int(input("Número 2: "))
 print(amigos(numero1,numero2))
except:
 print(" Ingrese un Número")

