#Ordenar tres números
A=int(input("primer numero "))
B=int(input("segundo numero "))
C=int(input("tercer numero "))
if(A<=B and B<=C):
 print(A,",",B,",",C)
elif(A<=C and C<=B):
 print(A,",",C,",",B)
elif(B<=A and A<=C):
 print(B,",",A,",",C)
elif(B<=C and C<=A):
 print(B,",",C,",",A) 
elif(C<=A and A<=B):
 print(C,",",A,",",B)
elif(C<=B and B<=A):
  print(C,",",B,",",A)