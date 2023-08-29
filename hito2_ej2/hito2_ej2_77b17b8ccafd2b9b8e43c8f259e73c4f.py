ADN=input("Ingresa la palabra que quieras encriptar: ")

genoma = ['a', 'c', 't', 'g', 'A', 'C', 'T', 'G']
valido = True
for i in ADN:
  if not(i in genoma):
    valido = False

if valido:
  print("La secuencia "+ADN+" es correcta")
else:
  print('La secuencia '+ADN+" es incorrecta")