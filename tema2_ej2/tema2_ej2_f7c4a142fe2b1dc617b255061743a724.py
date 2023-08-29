def amigos(a,b): 
  div_de_numero=1 
  div_de_numero_1=1 
  suma_div_numero=0 
  suma_div_numero_1=0 
  while div_de_numero<a: 
    if a%div_de_numero==0: 
      suma_div_numero+=div_de_numero 
      print("divisor de %d es: %d" % (a,div_de_numero),"la suma de divisores de %d es: %d" %(a,suma_div_numero)) 
    div_de_numero+=1 
  while div_de_numero_1<b: 
    if b%div_de_numero_1==0: 
      suma_div_numero_1+=div_de_numero_1
      print("divisor de %d es: %d" % (b,div_de_numero_1),"la suma de divisores de %d es: %d" %(b,suma_div_numero_1)) 
    div_de_numero_1 += 1 
  if suma_div_numero==b and suma_div_numero_1==a: 
    return True 
  else: 
    return False 
try: 
 numero = int(input("Número 1: ")) 
 numero_1 = int(input("Número 2: ")) 
 print(amigos(numero,numero_1)) 
except: 
 print("Ingrese un Número")