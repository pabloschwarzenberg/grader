# por favor escribe aquí tu funci
def es_primo(n):

  if(n>1):

    x=0
    div=2

    while(div<n):
      resto = n%div
      if(resto==0):
        x= x+1
      div= div+1

    if(x==0):
      return True
    else:
      return False
  else:
    return False
try:
  n2=int(input("Ingrese un número: "))
  print(es_primo(n2))
except:
  print("-----ERROR-------")