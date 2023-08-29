# completa el código de la función
def suma_divisores(a):
  divisores=[0]
  for i in range(1, a+1):
    if(a%i==0):
      divisores.append(i)
    x=(sum(divisores)-a) % 2==0
    if x==0:
      return ((sum(divisores)+a-2), True)

    else:
      return ((sum(divisores)+a-1), False)






           