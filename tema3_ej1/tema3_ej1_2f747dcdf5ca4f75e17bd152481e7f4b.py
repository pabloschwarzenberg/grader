# completa el código de la función
def suma_divisores(a):
  aa = []
  i = 2
  while i <= a:
    if a % i == 0:
      aa.append(a//i)
    i = i + 1 
  if sum(aa) == 1:
    return (sum(aa),True)
  if sum(aa) != 1:
    return (sum(aa),False)