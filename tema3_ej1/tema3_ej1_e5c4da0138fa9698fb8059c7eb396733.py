# completa el código de la función
import math
def suma_divisores(numero):
    suma = 0
    for i in range(1,numero):
      if numero%i==0:
        suma+=i
    if (numero<=1):
        return (suma,False)
    for i in range(2, math.ceil(math.sqrt(numero))+1):
        if(numero%i==0 and i!=numero):
            return (suma,False)
    return (suma,True)
    
if __name__ == "__main__": 
  numero = int(input("Ingrese número: "))
  primo = suma_divisores(numero)
  print (primo)