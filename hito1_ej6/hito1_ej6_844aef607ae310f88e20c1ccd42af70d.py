#Ordenar tres números
a = eval(input('Numero 1: '))
b = eval(input('Numero 2: '))
c = eval(input('Numero 3: '))

if (a <= b) and (a<=c):
  menor = a
  if b<=c:
    medio = b
    mayor = c
  else:
    medio = c
    mayor = b
elif b<=a and b<=c:
  menor = b
  if a<=c:
    medio = a
    mayor = c
  else:
    medio = c 
    mayor = a
else:
  menor = c
  if a<=b:
    medio = a
    mayor = b
  else:
    medio = b
    mayor = a

print(menor,",",medio,",",mayor)
