# completa el código de la función
def amigos(a,b):
  num=0
  lista_a=[]
  sonamigos=True
  if a==b:
    return False
  if a==1 or b==1:
    return False
  divisor=1
  while divisor < a :
    if a%divisor==0:  
      num=a//divisor
      if num==a:
        num=0
      else:
        num=str(num)
        lista_a.append(num)
    divisor += 1
  lista_a.append(1)
  i=0
  suma=0
  while i <= len(lista_a)-1:
    num=lista_a[i]
    num=int(num)
    suma=num+suma
    i+=1
  if suma==b:
    return True
  else:
    return False
