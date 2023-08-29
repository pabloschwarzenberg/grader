# completa el código de la función
def add(a, b):
  return a + b

def amigos(a, b):
    if add(divisores(a)) == b and add(divisores(b)) == a:
        return True
    else:
        return False
    
def divisores(num):
    return [x for x in range(1, num) if num % x == 0]
    
def add(numeros):
    total = 0
    for num in numeros:
        total += num
    return total
    
amigos(220, 284)