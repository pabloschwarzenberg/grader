divisores=[1]
def numero_perfecto(a):
  divisores=[1]
  div=2
  n=1
  if a!=1:
    while div<a:
      if a%div==0:
        divisores.append(div)
      div+=1
    divs=sum(divisores)
    if divs==a:
      return True
    else:
      return False

  else:
    return True
        

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           