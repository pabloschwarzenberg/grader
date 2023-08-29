def numero_perfecto(a):
  divisor_candidato= 1
  b=0
  while divisor_candidato< a:
    if a%divisor_candidato==0:
      b=b+divisor_candidato
      divisor_candidato=divisor_candidato + 1
      continue
    else:
      divisor_candidato=divisor_candidato + 1
      continue
  
  if b==a:
    return True
  else:
    return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           
