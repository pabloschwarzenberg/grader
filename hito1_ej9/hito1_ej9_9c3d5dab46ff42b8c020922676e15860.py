#Sistema de Ecuaciones
A = eval(input("ingrese el valor para A: "))
B = eval(input("ingreese el valor para B: "))
C = eval(input("ingrese el valor para C: "))
D = eval(input("ingrese el valor para D: "))
E = eval(input("ingrese el valor para E: "))
F = eval(input("ingrese el valor para F: "))

det = A * E - B * D

if det != 0 :
    x = (E * C - B * F) / det
    y = (A * F - D * C) / det

    print("x=",(x))

    print("y=",(y))      