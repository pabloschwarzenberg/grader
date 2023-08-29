def solucion_sistema_de_ecuaciones(a, b, c, d, e, f):
    determinante = a*e - b*d
    if determinante !=0:
        x = (c*e - b*f) / determinante
        y = (a*f - c*d) / determinante
        print("x= ", x)
        print("y= ", y)
print("escriba los valores de a b c d e y f: ")
a, b, c, d, e, f = map(float, input().split())
print(solucion_sistema_de_ecuaciones(a, b, c, d, e, f))