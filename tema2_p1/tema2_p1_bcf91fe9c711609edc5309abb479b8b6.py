# por favor escribe aquí tu función
import math
def es_primo(n):
    if (n<=1):
        return False
    
    for i in range(2, math.ceil(math.sqrt(n))+1):
        if(n%i==0 and i!=n):
            return False
    return True
try:
  a = int(input("ingrese un numero:"))
  if es_primo(a):
    print("True")
  else:
    print("False")
except:
  print("No es entero")