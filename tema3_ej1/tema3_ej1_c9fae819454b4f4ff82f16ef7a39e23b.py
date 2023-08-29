# completa el código de la función
def suma_divisores(a):
  l=[]
  for i in range(1,a):
    if a%i==0:
      l.append(i)
  print(sum(l))
  if sum(l)==1:
    return (sum(l),True)
  else:
    return (sum(l),False)
  if __name__ == "__main__": 
    a=int(input("Ingrese su numero: "))
