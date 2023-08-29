#Ordenar tres números

#variables
a = int(input('Ingresa el primer numero: '))
b = int(input('Ingresa el segundo numero: '))
c = int(input('Ingresa el tercer numero: '))

#condiciones
if a < b and a < c and b < c:
    print(f'los numeros de menor a mayor son {a} {b} {c}')
elif a < b and a < c and b > c:
    print(f'Los numeros de menor a mayor son {a} {c} {b}')
elif b < a and b < c and a > c:
    print(f'Los numeros de menor a mayor son {b} {c} {a}')
elif b < a and b < c and a < c:
    print(f'Los numeros de menor a mayor son {b} {a} {c}')
elif c < a and c < b and a < b:
    print(f'Los numeros de menor a mayor son {c} {a} {b}')
else:
    print(f'Los numero de menor a mayor son {c} {b} {a}')
