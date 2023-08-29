# completa el código de la función
def suma_divisores(a):
  suma=0
  numero=1
  while numero<a:
    if a%numero==0:
      suma=suma+numero
      numero=numero+1
    else:
      numero=numero+1
# cuando solamente es divisible por el mismo y por 1 es primo y la suma es 1
  if suma==1:
    return (suma, True)
  else:
    return (suma, False)
          