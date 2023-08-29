# completa el código de la función
def amigos(a,b):
  div_de_n_1=1
  div_de_n_2=1
  suma_div_n_1=0
  suma_div_n_2=0
  while div_de_n_1<a:
    if a%div_de_n_1==0:
      suma_div_n_1+=div_de_n_1
      print("El divisor de %d: %d" % (a,div_de_n_1),"la suma de los divisores de %d: %d" %(a,suma_div_n_1))
    div_de_n_1+=1
  while div_de_n_2<b:
    if b%div_de_n_2==0:
      suma_div_n_2+=div_de_n_2
      print("El divisor de %d: %d" % (b,div_de_n_2),"la suma de los divisores de %d: %d" %(b,suma_div_n_2))
    div_de_n_2 += 1
  if suma_div_n_1==b and suma_div_n_2==a:
    return True
  else:
    return False
try:
 n_1 = int(input("Primero: "))
 n_2 = int(input("Segundo: "))
 print(amigos(n_1,n_2))
except:
 print("Ingrese un número: ")