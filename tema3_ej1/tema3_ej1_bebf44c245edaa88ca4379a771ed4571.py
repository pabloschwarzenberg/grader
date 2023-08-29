# completa el código de la función

divisores=[1]
def suma_divisores(a):
  divisores=[1]
  div=2
  n=1
  if a!=1:
    while div<a:
      if a%div==0:
        divisores.append(div)
      div+=1
    divs=sum(divisores)
    if divs==1:
      return 1, True
    else:
      return divs, False

  else:
    return 0, False
  
  
  
  
if __name__ == "__main__":
    a=int(input())
    print(suma_divisores(a))