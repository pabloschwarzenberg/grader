#Ordenar tres números
#ordenar de menor a mayor
n1 = eval(input('Ingrese el primer numero entero:'))
n2 = eval(input('Ingrese el segundo numero entero:'))
n3 = eval(input('Ingrese el tercer numero entero:'))
print('\n')

if n1<=n2<=n3:
    print('El orden de menor a mayor es:',n1,',',n2,',',n3)
elif n1<=n3<=n2:
    print('El orden de menor a mayor es:',n1,',',n3,',',n2)
elif n2<=n1<=n3:
    print('El orden de menor a mayor es:',n2,',',n1,',',n3)
elif n3<=n1<=n2:
    print('El orden de menor a mayor es:',n3,',',n1,',',n2)
elif n2<=n3<=n1:
    print('El orden de menor a mayor es:',n2,',',n3,',',n1)
elif n3<=n2<=n1:
    print('El orden de menor a mayor es:',n3,',',n2,',',n1)
