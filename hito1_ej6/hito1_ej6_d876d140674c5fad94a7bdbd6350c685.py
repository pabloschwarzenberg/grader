#Ordenar tres números
A = eval(input('ingrese el primer numero: '))
B = eval(input('ingrese el segundo numero: '))
C = eval(input('ingrese el tercer numero: '))

if A<=B<=C:
    print('El orden de menor a mayor es',A, ',', B, ',', C)

if B<=C<=A:
    print('El orden de menor a mayor es',B, ',', C, ',', A)

if C<=B<=A:
    print('El orden de menor a mayor es',C, ',', B, ',', A)

if C<=A<=B:
    print('El orden de menor a mayor es',C, ',', A, ',', B)

if A<=C<=B:
    print('El orden de menor a mayor es',A, ',', C, ',', B)

if B<=A<=C:
    print('El orden menor a mayor es',B, ',', A, ',', C)
 