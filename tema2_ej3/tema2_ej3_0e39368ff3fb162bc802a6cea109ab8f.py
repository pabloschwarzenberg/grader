def numero_perfecto(a):
  divisores=[]
  i=1
  while i<a:
    if a%i==0:
      divisores.append(i)
    i=i+1
  j=0
  suma=0
  while len(divisores)>j:
    suma=suma + divisores[j]
    j+=1
  if suma==a:
    return True
  else:
    return False       