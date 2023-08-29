N = int(input("ingrese un numero de hasta 4 digitos: "))
M = (N // 1000) % 10
C = (N // 100) % 10
D = (N // 10) % 10
U = (N // 1) % 10

if N < 10:
     print(U, "U")
if 10 <= N < 100:
     print(D, "D+", U, "U")
if 100 <= N < 1000:
     print(C, "C+", D, "D+", U, "U+")
if 1000 <= N < 10000:
     print(M, "M+", C, "C+", D, "D+", U, "U")
     
