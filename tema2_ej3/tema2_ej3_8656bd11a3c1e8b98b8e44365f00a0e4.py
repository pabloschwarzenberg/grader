def numero_perfecto(a):
  div = [0]
  
  for i in range(1, a):
    if a % i == 0:
      div.append(i)
  suma = sum(div)
  if suma == a:
    perfecto = True
  else:
    perfecto = False  
  
  return (perfecto)


if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           