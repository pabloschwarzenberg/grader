# completa el código de la función
def suma_divisores(a):
  contador=1
  contador2=0
  divisores=[]
  suma=0
  while contador<a:
    if a%contador==0:
      divisores.append(contador)
    contador+=1
    
  while contador2<len(divisores):
    suma=suma+divisores[contador2]
    contador2+=1
  if suma==1:
    w=True
  else:
    w=False
  return suma,w         