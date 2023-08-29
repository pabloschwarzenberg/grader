# completa el código de la función
def suma_divisores(a):
  divisor_candidato=1
  suma=0
  numero=int(a)
  while divisor_candidato<=numero:
      if numero%divisor_candidato==0 and divisor_candidato!=a:
          suma+=divisor_candidato
      divisor_candidato+=1   
  r="s"
  if suma>1:
    r=False
  elif suma<=1:
    if a==1:
      suma=0
      r=False
    else:
      r=True
  
  return suma,r