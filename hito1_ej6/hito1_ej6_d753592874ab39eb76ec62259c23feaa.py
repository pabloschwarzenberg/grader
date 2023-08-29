#Ordenar tres números
A=int(input("Ingrese número: "))
B=int(input("Ingrese número: "))
C=int(input("Ingrese número: "))
if A<B and A<C:
    if B<C:
        print("El orden de los números ordenados de menos a mayor es ", A,",",B,",",C)
    else:
        print("El orden de los números ordenados de menos a mayor es ",A,",",C,",",B)
if B<A and B<C:
    if A<C:
        print("El orden de los números ordenados de menos a mayor es ",B,",",A,",",C)
    else:
        print("El orden de los números ordenados de menos a mayor es ",B,",",C,",",A)
if C<A and C<B:
    if A<B:
        print("El orden de los números ordenados de menos a mayor es ",C,",",A,",",B)
    else:
        print("El orden de los números ordenados de menos a mayor es ",C,",",B,",",A)

