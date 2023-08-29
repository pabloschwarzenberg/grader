#francisco serra
A=int(input("ingrese el primer numero:"))
B=int(input("ingrese el segundo numero:"))
C=int(input("ingrese el tecer numero:"))
if A>B and A>C:
  if B>C:
    print (C,",",B,",",A)
  else: 
    print (B,",",C,",",A)
if B>C and B>A:
  if C>A:
    print (A,",",C,",",B)
  else:
    print (C,",",A,",",B)
if C>B and C>A:
  if A>B:
    print (B,",",A,",",C)
  else: 
    print (A,",",B,",",C)