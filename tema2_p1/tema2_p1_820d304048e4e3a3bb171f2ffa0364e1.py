# por favor escribe aquí tu función
import math

def esPrimo(n)
    if n<2
        return False
    for x in range(2, int(math.sqrt(n))+1)
        if n%x == 0:
            return False
            
    return True
  
def seriePrimo(numPrimo):
    c = 0
    i = 0
    while c < numPrimo:
        i += 1
        if esPrimo(i)
        c += 1
        print(i)
        
seriePrimo(1000)