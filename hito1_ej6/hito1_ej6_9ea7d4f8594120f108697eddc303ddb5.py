#Ordenar tres números
a=int(input("ingrese el primer numero:"))
print(a)
b=int(input("ingrese el segundo numero:"))
print(b)
c=int(input("ingrese el tercer numero:"))
print(c)
numeros=[]
if a<b and a<c:
  numeros.append(a)
  if b<c:
    numeros.append(b)
    numeros.append(c) 
  else:
    numeros.append(c)
    numeros.append(b)
if b<a and b<c:
  numeros.append(b)
  if a<c:
    numeros.append(a)
    numeros.append(c) 
  else:
    numeros.append(c)
    numeros.append(a)
if c<a and c<b:
  numeros.append(c)
  if b<a:
    numeros.append(b)
    numeros.append(a) 
  else:
    numeros.append(a)
    numeros.append(b) 
print(numeros[0],",",numeros[1],",",numeros[2])     