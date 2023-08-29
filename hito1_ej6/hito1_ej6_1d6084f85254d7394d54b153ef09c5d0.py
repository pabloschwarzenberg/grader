#Ordenar tres números
a=int(input('Escribe 1° numero:'))
b=int(input('Escribe 2° numero:'))
c=int(input('Escribe 3° numero:'))

minimo=min(a,b,c)
maximo=max(a,b,c)
intermedio=(a+b+c)-minimo-maximo


print('Los numeros ingresados ordenados son:{},{},{}'.format(minimo,intermedio, maximo))


      