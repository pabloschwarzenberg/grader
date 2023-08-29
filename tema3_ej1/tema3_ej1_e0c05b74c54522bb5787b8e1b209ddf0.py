def suma_divisores(a):
  contador_1=0
  contador_2=a-1
  while contador_2>=1:
    if a%contador_2==0:
      contador_1=contador_1+contador_2
      contador_2=contador_2-1
    else:
      contador_2=contador_2-1
  if a==1:
    return 0, False
  if contador_1==1:
    b=True
  else:
    b=False
  
  
  return contador_1,b
           