def lista_divisores(c):
  divisores = []
  for i in range(1, c-1):
      if c % i == 0:
          divisores.append(i)
  return divisores
  
def suma_divisores(divisores):
  suma = 0
  for i in range(0, len(divisores)):
    suma = suma + divisores[i]
  return suma  

def numero_perfecto(c):
  x = lista_divisores(c)
  y = suma_divisores(x)
  if y == c:
    return True
  else:  
    return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           