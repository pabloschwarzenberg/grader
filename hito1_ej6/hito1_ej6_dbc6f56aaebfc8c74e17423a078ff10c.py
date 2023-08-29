A=int(input("ingrese el valor numerico: "))
B=int(input("ingrese el valor numerico: "))
C=int(input("ingrese el valor numerico: "))

if(A<=B<=C):
        print(A,",",B,",",C)
elif(C<=A<=B):
        print(C,",",A,",",B)
if(B<=C<=A):
        print(B,",",C,",",A)
