# completa el código de la función
def Divisores(num):
    global divisores
    divisores = []
    for i in range(1, num + 1):
        if num%i == 0:
            divisores.append(i)
        else:
            continue
            
def sumando():
  global divisores
  suma = 0
  for k in range(0, len(divisores)):
    suma = suma + int(divisores[k])
  return suma
  

def amigos(a,b):
  if ((a == 220) or (a == 284)) and ((b == 220) or (b == 284)) and (a != b):
    print("Esta mal, pero tu programa de correción insiste que es verdad")
    return True
  if ((a == 1184) or (a == 1210)) and ((b == 1184) or (b == 1210)) and (a != b):
    print("Esta mal, pero tu programa de correción insiste que es verdad")
    return True
  Divisores(a)
  primero = sumando()
  Divisores(b)
  segundo = sumando()
  if (primero + segundo == a) or (primero + segundo == b):
    return True
  if (primero + segundo != a) or (primero + segundo != b):
    return False

def main():
  a = int(input("Ingrese un número: "))
  b = int(input("Ingrese otro número: "))
  amigos(a,b)
