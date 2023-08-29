def suma_divisores(a):
  suma = 0
  for num in range(1,a):
    if a % num == 0:
      suma += num
  return suma
  
  
def numero_perfecto(a):
  if suma_divisores(a) == a:
    return True
  else:
    return False
  

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           