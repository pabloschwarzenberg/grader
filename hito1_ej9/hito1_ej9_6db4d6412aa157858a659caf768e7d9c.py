a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
det = a * e - b * d
if det != 0 :
    x = (e * c - b * f) / det
    y = (a * f - d * c) / det
    print("x=",round(x,1))
    print("y=",round(y,1))
else :
    m = d / a
    if m * c == f :
        print("El sistema tiene infinitas soluciones")
    else:
        print("El sistema no tiene soluciones")