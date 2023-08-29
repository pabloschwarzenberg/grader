#Ordenar tres números
print('** ORDENAR NÚMEROS ENTEROS **')
a = int(input('Ingrese el primer número: '))
b = int(input('Ingrese el segundo  número: '))
c = int(input('Ingrese el tercer número: '))
if a>=b and b>=c:
    print(str(c)+','+str(b)+','+str(a))
elif a>=c and c>=b:
    print(str(b)+','+str(c)+','+str(a))
elif b>=a and a>=c:
    print(str(c)+','+str(a)+','+str(b))
elif b>=c and c>=a:
    print(str(a)+','+str(c)+','+str(b))
elif c>=a and a>=b:
    print(str(b)+','+str(a)+','+str(c))
elif c>=b and b>=a:
    print(str(a)+','+str(b)+','+str(c))