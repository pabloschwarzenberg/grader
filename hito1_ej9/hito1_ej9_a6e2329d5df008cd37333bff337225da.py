#Sistema de Ecuaciones
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
##ax+by=c ; dx+ey=f
if a!=0:

        A = a * d
        B = b * d
        C = c * d
        D = d * (-a)
        E = e * (-a)
        F = f * (-a)

        y = (C+F)/(B+E)
        x = (c-(b*y))/a
        print("x="+str(x))
        print("y="+str(y))