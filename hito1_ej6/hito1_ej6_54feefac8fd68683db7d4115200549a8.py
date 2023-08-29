A = int(input("ingrese un numero: "))
B = int(input("ingrese un numero: "))
C = int(input("ingrese un numero: "))
if A == B == C:
  print("el orden es: ",A,",",B,",",C,)

if A == B > C:
  print("el orden es: ",C,",",B,",",A,)

if A > B == C:
  print("el orden es: ",C,",",B,",",A,)

if A == B < C:
  print("el orden es: ",A,",",B,",",C,)

if A < B == C:
  print("el orden es: ",A,",",C,",",B,)

if A == C < B:
  print("el orden es: ",A,",",C,",",B,)

if A == C > B:
  print("el orden es: ",B,",",C,",",A,)

if A < B < C:
  print("el orden es: ",A,",",B,",",C,)

if C < B < A:
  print("el orden es: ",C,",",B,",",A,)

if B < A < C:
  print("el orden es: ",B,",",A,",",C,)

if C < A < B:
  print("el orden es: ",C,",",A,",",B,)

if B < C < A:
  print("el orden es: ",B,",",C,",",A,)

if A < C < B:
  print("el orden es: ",A,",",C,",",B,)