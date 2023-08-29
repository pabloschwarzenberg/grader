#Factores Primos
factores = []
nro = int(input())
for x in range(2, nro + 1):
  if nro % x == 0:
    for y in range(2, x+1):
      if x % y == 0 and x != y:
        break
      elif y == x:
        factores.append(x)
        suma = 1
        for u in factores:
          suma = suma * u
        while suma < nro:
          suma = suma * x
          if suma == nro:
            factores.append(x)
for a in factores:
  print(a)
        
            
          