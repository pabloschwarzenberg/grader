# completa el código de la función
def amigos(a,b):
  division_de_Numero_1=1
  division_de_Numero_2=1
  suma_div_Numero_1=0
  suma_div_Numero_2=0
  while division_de_Numero_1<a:
    if a%division_de_Numero_1==0:
      suma_div_Numero_1+=division_de_Numero_1
      print("divisor de %d es: %d" % (a,division_de_Numero_1),"la suma de divisores de %d es: %d" %(a,suma_div_Numero_1))
    division_de_Numero_1+=1
  while division_de_Numero_2<b:
    if b%division_de_Numero_2==0:
      suma_div_Numero_2+=division_de_Numero_2
      print("divisor de %d es: %d" % (b,division_de_Numero_2),"la suma de divisores de %d es: %d" %(b,suma_div_Numero_2))
    division_de_Numero_2 += 1
  if suma_div_Numero_1==b and suma_div_Numero_2==a:
    return True
  else:
    return False
try:
 Numero_1 = int(input("Número 1: "))
 Numero_2 = int(input("Número 2: "))
 print(amigos(Number_1,Number_2))
except:
 print("Ingrese un Número")