#Ordenar tres números
n1=int(input('Ingrese primer numero: '))
print('')
n2=int(input('Ingrese segundo numero: '))
print('')
n3=int(input('Ingrese tercer numero: '))

z=[n1,n2,n3]
ordenado=sorted(z)

z1=ordenado[0]
z2=ordenado[1]
z3=ordenado[2]

print('')
print('Numeros ordenados de menor a mayor: '+str(z1)+', '+str(z2)+', '+str(z3))     