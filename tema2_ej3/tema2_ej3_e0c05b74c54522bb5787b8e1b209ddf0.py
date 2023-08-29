def numero_perfecto(a):
  contador_1=0
  contador_2=a-1
  while contador_2>=1:
    if a%contador_2==0:
      contador_1=contador_1+contador_2
      contador_2=contador_2-1
    else:
      contador_2=contador_2-1
  if contador_1==a:
    return True
  else:
    return False

           