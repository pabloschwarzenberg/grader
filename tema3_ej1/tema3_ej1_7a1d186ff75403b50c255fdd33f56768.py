# completa el código de la función
def suma_divisores(a):
  division=[i for i in range(1,a)
  if a%i==0]
  m=sum(division)
  if m ==1:
    return m, True
  return m, False
           