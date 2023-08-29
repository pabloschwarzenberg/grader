# por favor escribe aquí tu función
def es_primo(n):
  divisor=1
  c_div=0
  while divisor <= n:
    if n%divisor ==0:
       print(divisor)
       c_div = c_div + 1
    divisor = divisor +1
  if c_div==2:
     return True
  else:
       return False
  

         
           