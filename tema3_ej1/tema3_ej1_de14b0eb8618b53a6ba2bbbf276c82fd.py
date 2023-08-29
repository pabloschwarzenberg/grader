# completa el código de la función
def suma_divisores(a):
  es_primo=False
  suma_divisores=0
  for i in range(1,a):
    if a%i==0:
      suma_divisores=suma_divisores+i
  if suma_divisores==1:
    es_primo=True
  return (suma_divisores,es_primo)
           