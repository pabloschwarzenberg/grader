def solucion(a, b, c, d, e, f):
  determinante = a*e - b*d
  if determinante != 0:
    x = (c*e - b*f) / determinante
    y = (a*f - c*d) / determinante
    x = round(x, 1)
    y = round(y, 1)
    print("x = ", x, "y = ", y)
        
    return x, y
  else:
    return false 

a = float(input("valor de a: "))
b = float(input("valor de b: "))
c = float(input("valor de c: "))
d = float(input("valor de d: "))
e = float(input("valor de e: "))
f = float(input("valor de f: "))

print(solucion(a, b, c, d, e, f))
