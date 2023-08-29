def amigos(a, b):
  return sum(divisores(a)) == b and sum(divisores(b)) == a
    
def divisores(n):
  return [i for i in range(1, n) if n % i == 0]
      
amigos(220, 284)
