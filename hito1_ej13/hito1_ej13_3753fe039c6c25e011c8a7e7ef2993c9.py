y=int(2)
#los numeros primos empiezan del 2 en adelante sin incluir el 1 ya que este mismo no es primo
n=int(input("introduzca su numero para calcular sus factores primos:"))
while(n!=1):
  if(n % y==0):
    print(str(y) + "");
    n=n/y;
  else:
    y=y+ 1