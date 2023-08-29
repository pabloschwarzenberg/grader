#reciba tres números enteros y los imp ordenados de menor a mayor, separados por una coma.

#Encabezado
print("====================")
print('Ordenador de numeros')
print("====================")

#Asignar valor a variables + pedir informacion
a = int(input('Ingrese el primer numero: ' ))
b = int(input('Ingrese el segundo numero: '))
c = int(input('Ingrese el tercer numero: '))

#condiciones
if a <= b <= c:
    print('El orden de menor a mayor es: ',a,',',b,',',c)
elif a<=c<=b:
    print('El orden de menor a mayor es: ',a,',',c,',',b)
elif b<=c<=a:
    print('El orden de menor a mayor es: ',b,',',c,',',a)
elif b<=a<=c:
    print('El orden de menor a mayor es: ',b,',',a,',',c)
elif c<=a<=b:
    print('El orden de menor a mayor es: ',c,',',a,',',b)
else :
    print('El orden de menor a mayor es: ',c,',',b,',',a)
print("fin.")