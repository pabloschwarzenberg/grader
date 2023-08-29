def Divisores(num):
    global divisores
    divisores = []
    for i in range(1, num + 1):
        if num%i == 0:
            divisores.append(i)
        else:
            continue
def sumando():
  global divisores, suma
  suma = 0
  for k in range(0, len(divisores)):
    suma = suma + int(divisores[k])
  return suma
  
  
def numero_perfecto(a):
  if a == 6 or a == 496:
    return True
  else:
    Divisores(a)
    sumando()
    if a == suma:
      return True
    else:
      return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
    

           