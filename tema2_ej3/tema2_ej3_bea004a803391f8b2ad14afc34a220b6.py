def numero_perfecto(a):
  divisores = 1
  perfecto = False
  for i in range(2,a+1):
    if a%i == 0:
      divisores += i
  if divisores-a == a:
    perfecto = True
  return perfecto

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           