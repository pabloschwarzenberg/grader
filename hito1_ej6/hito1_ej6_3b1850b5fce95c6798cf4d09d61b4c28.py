#Ordenar tres números
A= int(input(" ingrese el primer numero:"))
B= int(input(" ingrese el segundo numero:"))
C= int(input(" ingrese el tercer numero:"))
if (A>=B>=C):
    print([int(C), int(B), int(A)])
elif (A>=C>=B):
    print([int(B), int(C), int(A)])
elif (B>=A>=C):
    print([int(C), int(A), int(B)])
elif (B>=C>=A):
    print([int(A), int(C), int(B)])
elif (C>=A>=B):
    print([int(B), int(A), int(C)])      
elif (C>=B>=A):
    print([int(A), int(B), int(C)])       