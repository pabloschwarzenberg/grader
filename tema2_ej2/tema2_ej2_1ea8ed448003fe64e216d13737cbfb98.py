def amigos(x,y):
  div_de_numero_1=1
  div_de_numero_2=1
  suma_div_numero_1=0
  suma_div_numero_2=0
  while div_de_numero_1<x:
    if x%div_de_numero_1==0:
      suma_div_numero_1+=div_de_numero_1
    div_de_numero_1+=1
  while div_de_numero_2<y:
    if y%div_de_numero_2==0:
      suma_div_numero_2+=div_de_numero_2
    div_de_numero_2 += 1
  if suma_div_numero_1==y and suma_div_numero_2==x:
    return True
  else:
    return False
try:
 num1 = int(input("Número 1: "))
 num2 = int(input("Número 2: "))
 print(amigos(num1,num2))
except:
 print("Por favor Ingrese un Número")           