#Sistema de Ecuaciones
A = []
for i in range(6):
    a = int(input())
    A.append(a)
a1 = A[0]
a2 = A[1]
a3 = A[2]
a4 = A[3]
a5 = A[4]
a6 = A[5]
y = ((a6*a1)-a3)/(-a2+(a5*a1))
x = (a6-(a5*y))/a4
print("['x="+str(x)+"', 'y="+str(y)+"']")