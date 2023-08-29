# completa el código de la función
def suma_divisores(a):
  suma=0
  for i in range(1,a):
    if a % i ==0:
       suma= suma+i
       
       
  b=True
  if a <= 1:
    b = False
  elif a == 2:
      b=True
  else:
     for i in range(2,a):
       if a % i ==0:
         b=False
  return(suma,b)
           