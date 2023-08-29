def ecuacion(n1,n2,n3,n4,n5,n6):
    det= (n1*n5) - (n2*n4)
    if det != 0:
        x = (n3*n5 - n2*n6)/det
        y = (n1*n6 - n3*n4)/det
        return print("['x=",x,"']",",","['y=",y,"']")
    else:
        return print("No tiene solución , prueba con otros numeros")

print("Ingrese numeros para el sistema de ecuaciones ")
n1=int(input("Ingrese el primer numero para la primera ecuación: "))
n2=int(input("Ingrese el segundo numero para la primera ecuación: "))
n3=int(input("Ingrese el resultado de la primera ecuación: "))
n4=int(input("Ingrese el primer numero para la segunda ecuación: "))
n5=int(input("Ingrese el segundo numero para la segunda ecuación: "))
n6=int(input("Ingrese el resultado de la segunda ecuación: "))
print(ecuacion(n1,n2,n3,n4,n5,n6))    