#Descomponer un número

numero = int(input("Ingrese un numero hasta 4 cifras: "))

#Descomposición
if numero < 10:
  #el numero es de 1 cifra
  numero = str(numero)
  uni = numero[0]
  print(uni,"U =", int(numero)) 

elif numero < 100:
  #el numero es de 2 cifras
  numero = str(numero)
  dec = numero[0]
  uni = numero[1]
  print(dec, "D +", uni,"U =", int(numero))

elif numero < 1000:
  #el numero es de 3 cifras
  numero = str(numero)
  cent = numero[0]
  dec = numero[1]
  uni = numero[2]
  print(cent, "C +",dec,"D +", uni,"U =", int(numero))

elif numero < 10000:
  numero = str(numero)
  mil = numero[0]
  cent = numero[1]
  dec = numero[2]
  uni = numero[3]
  print(mil,"M +",cent,"C +",dec,"D +",uni,"U =", int(numero))