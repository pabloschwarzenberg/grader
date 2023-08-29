#Descomponer un número
n = int(input("ingresar numero: "))
M = n // 1000
C = n // 100 % 10
D = n // 10 % 10
U = n % 10

M = str(M)
C = str(C)
D = str(D)
U = str(U)

m = M + "M"
c = C + "C"
d = D + "D"
u = U + "U"

if 1000 <= n <= 10000:
    print(m , "+", c , "+", d , "+", u)
elif 100 <= n <= 1000:
    print(c , "+", d , "+", u)
elif n <= 100:
    print(d , "+", u)
elif n <= 10:
    print(u)   