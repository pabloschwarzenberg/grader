# completa el código de la función
def amigos(l,v):
  numero_1=1
  numero_2=1
  suma_1=0
  suma_2=0
  while numero_1<l:
    if l%numero_1==0:
      suma_1+=numero_1
      print("divisor de %d es: %d" % (l,numero_1),"la suma de divisores de %d es: %d" %(l,suma_1))
    numero_1+=1
  while numero_2<v:
    if v% numero_2==0:
      suma_2+=numero_2
      print("divisor de %d es: %d" % (v,numero_2),"la suma de divisores de %d es: %d" %(v,suma_2))
    numero_2 += 1
  if suma_1==v and suma_2==l:
    return True
  else:
    return False
try:
 num_1 = int(input("Número 1: "))
 num_2 = int(input("Número 2: "))
 print(amigos(num_1,num_2))
except:
 print("Por favor Ingrese un Número")