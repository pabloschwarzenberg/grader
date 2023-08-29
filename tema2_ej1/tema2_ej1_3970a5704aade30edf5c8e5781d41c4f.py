def area_cuadrado(L):
    area=L**2
    return print(area)
def area_circulo(R):
    area=math.pi*R**2
    return print("%.3f" % area)
def area_triangulo(b,h):
    area=b*h/2
    return print(area)
def area_trapecio(B,b,h):
    area=(B+b)*h/2
    return print(area)
def area_rectangulo(b,h):
    area=b*h
    return print(area)
def area_eclipse(a,b):
    area=a*b*math.pi
    return print("%.3f" % area)