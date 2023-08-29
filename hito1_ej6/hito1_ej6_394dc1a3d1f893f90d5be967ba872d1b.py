A = int(input("Ingrese el primer número entero:"))
B = int(input("Ingrese el segundo número entero:"))
C = int(input("Ingrese el tercer número entero:"))
a = str(A)
b = str(B)
c = str(C)
if A < B < C or A == B < C:
  print (a + "," + b + "," + c)
elif A < C < B or A == C < B:
  print (a + "," + c + "," + b)
elif B < A < C or B == A < C:
  print(b + "," + a + "," + c)
elif B < C < A or B == C < A:
  print(b + "," + c + "," + a)
elif C < A < B or C == A < B:
  print(c + "," + a + "," + b)
elif C < B < A or C == B < A:
  print(c + "," + b + "," + a)
elif A == C > B:
  print(c + "," + a + "," + b)
elif B == C > A:
  print(c + "," + b + "," + a)
elif A == B > C:
  print(a + "," + b + "," + c)
elif A == C < B:
  print(b + "," + a + "," + c)
elif B == C < A:
  print(a + "," + b + "," + c)
elif A == B < C:
  print(c + "," + b + "," + a)