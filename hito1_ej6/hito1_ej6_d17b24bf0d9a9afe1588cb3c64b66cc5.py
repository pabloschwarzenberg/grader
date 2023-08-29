#Ordenar tres números
A = int(input("Ingrese el primer número: "))
B = int(input("Ingrese el segundo número: "))
C = int(input("Ingrese el tercer número: "))

if ((A<B and A<C) and (C<B and C>A)):
    print("los números ordenados de menor a mayor son:{}, {}, {}".format(A, C, B))
else:
    if((A<B and A<C) and (B<C and B>A)):
        print("los números ordenados de menor a mayor son: {}, {}, {}".format(A, B, C))
    else:
        if ((A < B and A == C) and (C < B and (C == A))):
            print("los números ordenados de menor a mayor son: {}, {}, {}".format(A, C, B))
        else:
            if ((A > B and A == C) and (C > B and C == A)):
                print("los números ordenados de menor a mayor son: {}, {}, {}".format(B, A, C))

if ((B<A and B<C) and (A<C and A>B)):
    print("los números ordenados de menor a mayor son: {}, {}, {}".format(B, A, C))
else:
    if((B<A and B<C) and (C<A and C>B)):
        print("los números ordenados de menor a mayor son: {}, {}, {}".format(B, C, A))
    else:
        if ((B < A and B == C) and (C < A and C == B)):
            print("los números ordenados de menor a mayor son: {}, {}, {}".format(B, C, A))
        else:
            if ((B > A and B == C) and (C > A and C == B)):
                print("los números ordenados de menor a mayor son: {}, {}, {}".format(A, B, C))

if ((C<B and C<A) and (B<A and B>C)):
    print("los números ordenados de menor a mayor son: {}, {}, {}".format(C, B, A))
else:
    if((C<B and C<A) and (A<B and A>C)):
        print("los números ordenados de menor a mayor son: {}, {}, {}".format(C, A, B))
    else:
        if ((C < B and B == A) and (C < A and A == B)):
            print("los números ordenados de menor a mayor son: {}, {}, {}".format(C, A, B))
        else:
            if ((C > B and B == A) and (C > A and A == B)):
                print("los números ordenados de menor a mayor son: {}, {}, {}".format(A, B, C))

if(A==B and B==C and C==A):
    print("los números ordenados de menor a mayor son: {}, {}, {}".format(A, B, C))  