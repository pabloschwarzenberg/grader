#Descomponer un número
numero = input()
desc = []
if int(numero) > 999:
  letras = ["M", "C", "D", "U"]
  num_lst = list(numero)
  for numero, letra in zip(num_lst, letras):
    desc.append(numero + letra)
  print(" + ".join(desc))

elif int(numero) > 99:
  letras = ["C", "D", "U"]
  num_lst = list(numero)
  for numero, letra in zip(num_lst, letras):
    desc.append(numero + letra)
  print(" + ".join(desc))

elif int(numero) > 9:
  letras = ["D", "U"]
  num_lst = list(numero)
  for numero, letra in zip(num_lst, letras):
    desc.append(numero + letra)
  print(" + ".join(desc))

elif int(numero) > 0:
  print(numero + "U")