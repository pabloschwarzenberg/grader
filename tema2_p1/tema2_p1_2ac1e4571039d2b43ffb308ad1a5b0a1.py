def es_primo(num):

  if num >1:
    x=0
    div=2

    while div<num:
      resto = num%div

      if resto==0:
        x+=1
      div+=1

    if x==0:
      return True

    else:
      return False

  else:
    return False

try:
  num_de_ingreso = int(input("Ingrese número: "))
  print(es_primo(num_de_ingreso))

except:
  print("Ingrese sólo número")
