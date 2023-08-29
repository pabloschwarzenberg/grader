def numero_perfecto(a):
    division = [i for i in range(1,a) if a%i == 0]
  suma = sum(division)
  if suma == a:
    return suma,True
  return suma,False
           