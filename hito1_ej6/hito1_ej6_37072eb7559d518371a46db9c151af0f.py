#Ordenar tres númeroas
a = int(input("ingrese el primer numero: "))
b = int(input("ingrese el segundo numero: "))
c = int(input("ingrese el tercer numero: "))
#desarrollo
if a >= b and a >= c:
  mayor = a
  if b > c:
   medio = b
   menor = c
  else:
   medio = c
   menor = b
if b >= c and b >= a:
  mayor = b
  if a > c:
   medio = a
   menor = c
  else: 
   medio = c
   menor = a
if c >= b and c >= a:
  mayor = c
  if b > a:
   medio = b
   menor = a
  else: 
   medio = a
   menor = b
 
print("el orden creciente de los numeros es:", menor,(","), medio,(","), mayor)