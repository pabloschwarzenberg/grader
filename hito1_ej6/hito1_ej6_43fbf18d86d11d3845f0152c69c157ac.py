#Ordenar tres números
a = input ("ingrese numero 1: ")
b = input ("ingrese numero 2: ")
c = input ("ingrese numero 3: ")
if a < b and b < c:
  print("el orden de los numeros es:" + str(a), str(b), str(c))
if a < c and c < b:
  print("el orden de los numeros:" + str(a), str(c), str(b))  
if b < a and a < c:
  print("el orden de los numeros:" + str(b), str(a), str(c))
if b < c and c < a:
  print("el orden de los numeros:" + str(b), str(c), str(a))
if c < a and a < b:
  print("el orden de los numeros:" + str(c), str(a), str(b))
if c < b and b < a:
  print("el orden de los numeros:" + str(c), str(b), str(a))    