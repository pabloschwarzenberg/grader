#Ordenar tres números
A=int(input("Ingrese el primer número: "))
B=int(input("Ingrese el segundo número: "))
C=int(input("Ingrese el tercer número: "))
if A>=B>=C : 
  print(C,",",B,",",A)
if B>=A>=C : 
  print(C,",",A,",",B)
if A>=C>=B : 
  print(B,",",C,",",A)
if C>=A>=B : 
  print(B,",",A,",",C)
if B>=C>=A : 
  print(A,",",C,",",B)
if C>=B>=A : 
  print(A,",",B,",",C)




