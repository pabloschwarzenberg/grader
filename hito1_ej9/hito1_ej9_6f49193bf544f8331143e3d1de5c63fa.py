def sistema_de_ecuaciones():
    a1= float(input("Ingrese el coeficiente de x en la primera ecuación: "))
    b1 = float(input("Ingrese el coeficiente de y en la primera ecuación: "))
    c1 = float(input("Ingrese el término independiente en la primera ecuación: "))
    a2 = float(input("Ingrese el coeficiente de x en la segunda ecuación: "))
    b2 = float(input("Ingrese el coeficiente de y en la segunda ecuación: "))
    c2 = float(input("Ingrese el término independiente en la segunda ecuación: "))
    
    determinante=a1*b2-a2*b1
    if determinante != 0:
        x = (c1 * b2 - c2 * b1) / determinante
        y = (a1 * c2 - a2 * c1) / determinante
        print("Las soluciones del sistema son:")
        print("x =", round(x, 1))
        print("y =", round(y, 1))
    else:
        print("El sistema no tiene solución única.")
        
    return
sistema_de_ecuaciones()
