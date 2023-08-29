def numero_perfecto(a):    
  divisor_candidato=1
  suma=0
  numero=int(a)
  while divisor_candidato<numero:
      if numero%divisor_candidato==0:
          suma+=divisor_candidato
      divisor_candidato+=1   
  r="s"
  if a==1:
      r=True
  else:
      if suma==a:
        r=True
      elif suma!=a:
        r=False
    
  return r

if __name__=="__main__":
  pass