def sistema(a, b, c, d, e, f):
    determinante = a*e - b*d

    if determinante != 0:
        x = (c*e - b*f)/ determinante
        y= (a*f - c*d) / determinante
        return x, y
    else:
        return None,None
print("Digiete los valores para a,b,c,d,e y f(ax + by = c / dx + ey = f): ")
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

print(sistema(a, b, c, d, e, f))

