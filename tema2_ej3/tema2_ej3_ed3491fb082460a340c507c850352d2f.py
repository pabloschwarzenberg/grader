def numero_perfecto(a):
  suma = 0
  if a == 1:
    suma = 0
    return suma,
  else:
    for i in range(1,a):
      if (a % i) == 0:
        suma = suma + i
    if suma == a:
      return True
    else:
      return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           

           