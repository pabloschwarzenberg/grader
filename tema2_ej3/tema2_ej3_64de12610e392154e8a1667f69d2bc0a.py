def numero_perfecto(a):
  suma = 0
  limite = a - 1
  for i in range(1, limite):
    if a % i == 0:
      suma += i
    else:
      suma += 0
  if suma == a:
    return True
  else:
    return False
 
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           