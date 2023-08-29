# completa el código de la función
def amigos(a,b):
  return sum([i for i in range(1,a) if a%i==0])==b and sum([i for i in range(1,b) if b%i==0])==a 
           