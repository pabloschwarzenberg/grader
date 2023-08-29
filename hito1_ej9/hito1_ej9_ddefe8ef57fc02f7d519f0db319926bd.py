#Sistema de Ecuaciones

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
if a/b != d/e :   
    x = (c*e - b*f) / (a*e - b*d)
    y = (a*f - c*d) / (a*e - b*d)
    print( "x=" + str(round(x,1)))
    print( "y=" + str(round(y,1)))
