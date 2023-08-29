# completa el código de la función
def amigos(a,b):
  div_de_Number_1=1 
  div_de_Number_2=1 
  suma_div_Number_1=0 
  suma_div_Number_2=0 
  while div_de_Number_1<a: 
    if a%div_de_Number_1==0: 
      suma_div_Number_1+=div_de_Number_1 
      print("divisor de %d es: %d" % (a,div_de_Number_1),"la suma de divisores de %d es: %d" %(a,suma_div_Number_1)) 
    div_de_Number_1+=1 
  while div_de_Number_2<b: 
    if b%div_de_Number_2==0: 
      suma_div_Number_2+=div_de_Number_2 
      print("divisor de %d es: %d" % (b,div_de_Number_2),"la suma de divisores de %d es: %d" %(b,suma_div_Number_2)) 
    div_de_Number_2 += 1 
  if suma_div_Number_1==b and suma_div_Number_2==a: 
    return True 
  else: 
    return False 
try: 
 Number_1 = int(input("Número 1: ")) 
 Number_2 = int(input("Número 2: ")) 
 print(amigos(Number_1,Number_2)) 
except: 
 print("Por favor Ingrese un Número")