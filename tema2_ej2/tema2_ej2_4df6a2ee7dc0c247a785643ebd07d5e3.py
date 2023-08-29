def amigos(a,b):
  dive_de_number_1=1 
  dive_de_number_2=1 
  suma_dive_number_1=0 
  suma_dive_number_2=0 
  while dive_de_number_1<a: 
    if a%dive_de_number_1==0: 
      suma_dive_number_1+=dive_de_number_1 
      print("divisor de %d es: %d" % (a,dive_de_number_1),"la suma de divisores de %d es: %d" %(a,suma_dive_number_1)) 
    dive_de_number_1+=1 
  while dive_de_number_2<b: 
    if b%dive_de_number_2==0: 
      suma_dive_number_2+=dive_de_number_2 
      print("divisor de %d es: %d" % (b,dive_de_number_2),"la suma de divisores de %d es: %d" %(b,suma_dive_number_2)) 
    dive_de_number_2 += 1 
  if suma_dive_number_1==b and suma_dive_number_2==a: 
    return True 
  else: 
    return False 
try: 
 number_1 = int(input("número 1: ")) 
 number_2 = int(input("número 2: ")) 
 print(amigos(number_1,number_2)) 
except: 
 print("Ingrese un número")