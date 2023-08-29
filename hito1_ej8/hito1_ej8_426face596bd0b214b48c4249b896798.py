#Descomponer un número
numero = str(input("ingrese un numero de maximo 4 digitos :"))

if(len(numero)<=4):
  resultado = ""
  descom = "UDCM"
  p_numero = len(numero)-1
  p_descom = 0
  while p_numero >= 0:
    if p_descom == 0:
      resultado = numero[p_numero] + descom[p_descom]
    else:
      resultado = numero[p_numero] + descom[p_descom] + " + " + resultado        

    p_descom = p_descom + 1
    p_numero = p_numero - 1

  print(resultado)
else:
  print("el número tiene más de 4 digitos")
  