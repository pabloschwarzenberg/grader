def amigos(a,b):
  div_numero=1
  div_numero_2=1
  suma_div_numero=0
  suma_div_numero_2=0
  while div_numero<a:
    if a%div_numero==0:
      suma_div_numero+=div_numero
    div_numero+=1
  while div_numero_2<b:
    if b%div_numero_2==0:
      suma_div_numero_2+=div_numero_2
    div_numero_2 += 1
  if suma_div_numero==b and suma_div_numero_2==a:
    return True
  else:
    return False
try:
 numero= int(input("Primero: "))
 numero_2 = int(input("Segundo: "))
 print(amigos(numero,numero_2))
except:
 print("Ingrese un número: ")
