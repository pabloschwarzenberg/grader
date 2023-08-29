# por favor escribe aquí tu función
def es_primo(num):
  div=2
  if num==1 or num==0:
    return False
  elif num==2:
    return True
  while div<num:
    if num%div==0:
      return False
    div+=1
    return True
print(es_primo)