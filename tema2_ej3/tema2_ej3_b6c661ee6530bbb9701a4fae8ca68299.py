def numero_perfecto(a):
  l = []
  largo = a-1
  for i in range(1,largo):
    if a%i == 0:
      l.append(i)        
  suma = sum(l)
  if suma == a:
      return True
  return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           