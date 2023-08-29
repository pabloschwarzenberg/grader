def sumDivisores(numero):
  contador = 0
  for divisor in range(1,numero-1):
    if (numero % divisor) == 0 :
      contador += divisor
 
  return contador

def numero_perfecto(a):
    return sumDivisores(a) == a

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           