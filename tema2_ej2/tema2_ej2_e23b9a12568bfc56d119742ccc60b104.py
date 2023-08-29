def amigos(a,b):
  div_num1=1
  div_num2=1
  suma_div=0
  suma_div2=0
  while div_num1<a:

    if a%div_num1==0:

      suma_div+=div_num1
    div_num1+=1

  while div_num2<b:

    if b%div_num2==0:

      suma_div2+=div_num2
    div_num2 += 1

  if suma_div==b and suma_div2==a:

    return True

  else:

    return False

try:

 n1=int(input("Número 1: "))

 n2=int(input("Número 2: "))

 print(amigos(n1,n2))
except:
 print("Ingrese un Número")