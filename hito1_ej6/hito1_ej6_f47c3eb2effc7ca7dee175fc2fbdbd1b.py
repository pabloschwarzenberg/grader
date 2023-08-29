#Ordenar tres números
#Sebastian Correa
A= int(input("ingrese el primer numero ",))
B= int(input("ingrese el segundo numero ",))
ZERO= int(input("ingrese el tercer numero ",))
if(A<=B<=ZERO):
  print(A,",",B,",",ZERO)
if(B<=A<=ZERO):
  print(B,",",A,",",ZERO)
if(A<=ZERO<=B):
  print(A,",",ZERO,",",B)
if(B<=ZERO<=A):
  print(B,",",ZERO,",",A)
if(ZERO<=A<=B):
  print(ZERO,",",A,",",B)
if(ZERO<B<A):
  print(ZERO,",",B,",",A)