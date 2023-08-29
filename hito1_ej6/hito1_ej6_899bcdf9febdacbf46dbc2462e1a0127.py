#Ordenar tres números
n1=int(input())
n2=int(input())
n3=int(input())
if n1 >= n2 and n1 >= n3:
  mayor = n1
  if n2 >= n3:
    mitad = n2
    menor = n3
  else:
    mitad = n3
    menor = n2  
elif n2 >= n1 and n2 >= n3:
  mayor = n2
  if n1 >= n3:
    mitad = n1
    menor = n3
  else:
    mitad = n3
    menor = n1  
else:
  mayor = n3  
  if n1 >= n2:
    mitad = n1
    menor = n2
  else:
    mitad = n2
    menor = n1
print(menor,",",mitad,",",mayor)