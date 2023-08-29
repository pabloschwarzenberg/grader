#Ordenar tres números
n1 = int(input('Número 1: '))
menor = n1
n2 = int(input('Número 2: '))
if ((n2 >= n1)):
  medio = n2
else:
  menor = n2
  medio = n1
n3 = int(input('Número 3: '))
if ((n3 <= n2) and (n3 >= n1)):
  medio = n3
  mayor = n2
  menor = n1
elif ((n3 <= n2) and (n3 <= n1)):
  menor = n3
  if ((n2 >= n1)):
    mayor = n2
    medio = n1
  else:
    medio = n2
    mayor = n1
else:
  mayor = n3

print(str(menor)+', '+str(medio)+', '+str(mayor))