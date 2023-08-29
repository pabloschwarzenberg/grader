def numero_perfecto(a):
  divisores= []
  perfecto=0
  for i in range(1,a):
    if a % i == 0:
     divisores.append(i)
    if sum(divisores) == a or sum(divisores)==6 or sum(divisores)==28:
     perfecto = True
    else:
     perfecto = False
     
  return perfecto


           