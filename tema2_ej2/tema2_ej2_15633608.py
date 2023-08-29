# completa el código de la función
def sum_div(a):
  suma = 0
  e = 1
  while e<a:
     if a%e==0:
       suma = suma + e
     e=e+1
  return suma

def amigos(a,b):
    if sum_div(a) == b and sum_div(b) == a:
        return True
    else:
        return False
           