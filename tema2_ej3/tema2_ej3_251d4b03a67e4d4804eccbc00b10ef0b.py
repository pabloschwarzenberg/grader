def numero_perfecto(perfect_number):
  contaitor=1
  adicion=0
  while contaitor!=perfect_number:
    if perfect_number%contaitor==0:
      adicion=adicion+contaitor
    contaitor=contaitor+1
  if adicion==perfect_number:
    return True
  else:
    return False

if __name__=="main":
  ingresed_number =eval(input("Ingrese el numero"))
  if numero_perfecto(ingresed_number):
    print("El numero {0} cae en perfecto".format(ingresed_number))
  else:
    print("El numero {0} no cae en perfecto".format(ingresed_number))