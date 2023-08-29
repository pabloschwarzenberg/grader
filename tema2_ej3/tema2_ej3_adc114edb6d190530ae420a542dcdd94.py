def perfecto(n):
    return divisores(n)==n
    
def divisores(n):
  suma=1
  for i in range(2,n):
    if n%i == 0: suma+=i
      if a==suma:
         return True
      else:
         return False