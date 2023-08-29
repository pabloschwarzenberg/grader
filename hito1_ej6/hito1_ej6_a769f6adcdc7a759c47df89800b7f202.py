#Ordenar tres números
n1 = eval(input('Ingrese el primer numero: '))
n2 = eval(input('Ingrese el segundo numero:'))
n3 = eval(input('Ingrese el tercer numero: '))


if n1 <= n2 <= n3:
  menor = n1
  medio = n2
  mayor = n3 
 
if n1 <= n3 <= n2:
  menor = n1
  medio = n3
  mayor = n2
  
if n2 <= n1 <= n3:
  menor = n2
  medio = n1
  mayor = n3 
if n2 <= n3 <= n1:
  menor = n2
  medio = n3
  mayor = n1
if n3 <= n1 <= n2:
  menor = n3 
  medio = n1
  mayor = n2
if n3 <= n2 <= n1: 
  menor = n3 
  medio = n2 
  mayor = n1
  
print('De menor a mayor es: '+str(menor)+','+str(medio)+','+str(mayor))