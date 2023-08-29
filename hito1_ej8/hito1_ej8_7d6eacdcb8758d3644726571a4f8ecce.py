M = 0
C = 0
D = 0
U = 0

n = input(" Ingresar número: ")
n = int(n)

while n >= 1000:
    n = n-1000
    M += 1
while n >= 100:
    n = n-100
    C += 1
while n >= 10:
    n = n - 10
    D += 1
while n >= 1:
    n = n - 1
    U += 1


if M > 0:
    print(str(M) + "M +" + str(C) + "C +" + str(D) + "D +" + str(U) + "U")
elif (M==0) and (C>0):
    print(str(C) + "C +" + str(D) + "D +" + str(U) + "U")
elif (M==0) and (C==0) and (D>0):
    print(str(D) + "D +" + str(U) + "U")
elif (M==0) and (C==0) and (D==0)and (U>0):
    print(str(U) + "U")

