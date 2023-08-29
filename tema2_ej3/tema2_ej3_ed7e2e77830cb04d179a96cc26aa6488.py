def numero_perfecto(a):
  i = 1
  acumulador = 0
  while i < a:
    if a%i == 0:
      acumulador = acumulador +i
    i = i+1
  if acumulador == a:
    return True
  else:
    return False

#if __name__=="__main__":
 #   a=int(input("Ingrese a: "))
  #  print(numero_perfecto(a))
           