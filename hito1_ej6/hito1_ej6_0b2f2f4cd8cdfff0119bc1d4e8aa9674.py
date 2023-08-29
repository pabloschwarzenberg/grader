#Ordenar tres números
  #Ordenar tres números
uno=int(input('Ingrese primer numero: '))
print('')
dos=int(input('Ingrese segundo numero: '))
print('')
tres=int(input('Ingrese tercer numero: '))

z=[uno,dos,tres]
ordenado=sorted(z)

z1=ordenado[0]
z2=ordenado[1]
z3=ordenado[2]

print('')
print('Numeros ordenados de menor a mayor: '+str(z1)+', '+str(z2)+', '+str(z3))    