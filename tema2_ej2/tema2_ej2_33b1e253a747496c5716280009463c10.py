# completa el código de la función
def amigos(a,b):
  return
def amigos(a,b):
  div_de_numero_1=1
  div_de_numero_2=1
  suma_div_numero_1=0
  suma_div_numero_2=0
  while div_de_numero_1<a:
    if a%div_de_numero_1==0:
      suma_div_numero_1+=div_de_numero_1
    div_de_numero_1+=1
  while div_de_numero_2<b:
    if b%div_de_numero_2==0:
      suma_div_numero_2+=div_de_numero_2
    div_de_numero_2 += 1
  if suma_div_numero_1==b and suma_div_numero_2==a:
    return True
  else:
    return False
try:
 numero_1 = int(input("Número 1: "))
 numero_2 = int(input("Número 2: "))
 print(amigos(numero_1,numero_2))
except:
 print("Por favor Ingrese un Número")       